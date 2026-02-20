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
    path("post/<int:pk>/delete/", delete_item, name="delete_item"),
    path("my_posts/", my_posts_view, name="user_posts"),
    path("comment/<int:pk>/delete/", delete_comment, name="delete_comment"),
    path("post/<int:post_id>/like/", like_post, name="like_post"),
    path("comment/<int:comment_id>/like/", like_comment, name="like_comment"),
    path("profile/<int:user_id>/", profile_view, name="profile"),
    # path("profile/<int:user_id>/edit/", ProfileEditView.as_view(), name="edit_profile"),
 ]
