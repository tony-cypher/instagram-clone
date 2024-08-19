from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.
def login(request):
    return render(request, 'users/login.html')

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('home')
    else:
        user_form = RegistrationForm()
        return render(request, 'users/register.html', {'user_form':user_form})