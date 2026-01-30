from django.urls import path
from .views import *

urlpatterns = [
    path("", ItemListView.as_view(), name="main_page"),
    path("login/", LoginView.as_view(), name="login"),
    path("registrate/", RegistrateView.as_view(), name="registrate"),
    path("logout/", LogoutView, name="logout"),
    path("delete_item/<int:pk>/", delete_item, name="delete_item"),
    path("chats/", chats_view, name="chats"),
    path("chats/<int:user_id>/", chats_view, name="chats"),
]

