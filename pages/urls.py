from django.urls import path
from .views import LoginView,RegistrateView, ItemListView

urlpatterns = [
    path("/",ItemListView.as_view(), name="main_page"),
    path('login/', LoginView.as_view(), name='login'),
    path('registrate/', RegistrateView.as_view(), name='registrate')

]
