from django.urls import path
from .views import *

urlpatterns = [
    path("",ItemListView.as_view(), name="main_page"),
    path('login/', LoginView.as_view(), name='login'),
    path('registrate/', RegistrateView.as_view(), name='registrate'),
    path('settings/', ItemListView.as_view(),name= 'settings'),
    path('chats/', ChatsListView.as_view(), name='chats'),
    path('logout/', LogoutView, name='logout'),
    path('delete_item/<int:pk>/', delete_item, name='delete_item'),

]