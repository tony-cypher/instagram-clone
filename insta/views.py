from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePage(TemplateView):
    template_name = 'insta/index.html'


class ProfilePage(TemplateView):
    template_name = 'insta/profile.html'


class UserPage(TemplateView):
    template_name = 'insta/user.html'
