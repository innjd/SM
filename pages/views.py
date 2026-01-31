from django.views.generic import ListView, FormView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Невірний логін або пароль')
            return self.form_invalid(form)

class RegistrateView(CreateView):
    template_name = 'registrate.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

def LogoutView(request):
    logout(request)
    return redirect('login')


class ItemListView(ListView):
    model = PostItem
    template_name = "main.html"
    context_object_name = "posts"
#//////////////////////////////////////////////////////////////

@login_required
def delete_item(request, pk):
    PostItem.objects.filter(pk=pk, author=request.user).delete()
    return redirect("user_posts")

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, author=request.user)
    post_id = comment.post.id
    comment.delete()
    return redirect("post_comments", post_id=post_id)

@login_required
def chats_view(request, user_id=None):
    users = User.objects.exclude(id=request.user.id).order_by("username")
    chat = None
    messages = None
    other_user = None
    if user_id is not None:
        other_user = get_object_or_404(User, id=user_id)
        if request.user.id < other_user.id:
            user1 = request.user
            user2 = other_user
        else:
            user1 = other_user
            user2 = request.user
        chat, _ = Chat.objects.get_or_create(user1=user1, user2=user2)
        messages = chat.messages.order_by("created_at")

        if request.method == "POST":
            text = request.POST.get("text", "").strip()
            if text:
                Message.objects.create(chat=chat, sender=request.user, text=text)
            return redirect("chat_detail", user_id=other_user.id)

    return render(request, "chats.html", {"users": users,"chat": chat,"messages": messages,"other_user": other_user,})

def post_coments_view(request, post_id):
    post = get_object_or_404(PostItem, id=post_id)
    comments = post.comments.order_by("created_at")

    if request.method == "POST":
        text = request.POST.get("text", "").strip()
        if text:
            Comment.objects.create(post=post,author=request.user,text=text)
        return redirect("post_comments", post_id=post.id)
    return render(request, "post_comments.html", {
        "post": post,
        "comments": comments
    })


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostItemForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("main_page")
    else:
        form = PostItemForm()
    return render(request, "create_post.html", {"form": form})

@login_required
def my_posts_view(request):
    posts = PostItem.objects.filter(author=request.user).order_by("-created_at")
    return render(request, "my_posts.html", {"posts": posts})