from django.urls import path
from .views import home, register, loginPage, logoutUser


urlpatterns = [
    path('',register, name="register"),
    path('login/',loginPage, name="login"),
    path('logout/',logoutUser, name="logout"),
    path('home/', home, name="home"),
]