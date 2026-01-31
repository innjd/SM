from django.urls import path
from .views import *

urlpatterns = [
    path("", ItemListView.as_view(), name="main_page"),
    path("login/", LoginView.as_view(), name="login"),
    path("registrate/", RegistrateView.as_view(), name="registrate"),
    path("logout/", LogoutView, name="logout"),
    path("chats/", chats_view, name="chats"),
    path("chats/<int:user_id>/", chats_view, name="chat_detail"),
    path("post/new/", create_post, name="create_post"),
    path("post/<int:post_id>/", post_coments_view, name="post_comments"),
]
