from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('<int:id>/profile/', views.index, name='profile'),
    path('post/<int:id>/profile/', views.post_user, name='post_user'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
