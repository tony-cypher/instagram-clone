from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('profile/', views.ProfilePage.as_view(), name='profile'),
    path('user/', views.UserPage.as_view(), name='user'),
]