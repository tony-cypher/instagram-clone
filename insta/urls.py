from django.urls import path
from . import views


urlpatterns = [
    path('', views.feed, name='home'),
    path('create/', views.post_create, name='create'),
    path('<int:id>/', views.feed, name='like'),
]