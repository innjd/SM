from django.views.generic import FormView, CreateView, ListView, TemplateView
from .forms import LoginForm
from .models import Post_Item
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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

class ItemListView(TemplateView):
    template_name = 'main.html'


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Post_Item, pk=pk)
    if request.method == "POST":
        item.delete()
    return redirect('edit_item_list')
