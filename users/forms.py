from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class':'form-control my-1', 'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'class':'form-control my-2', 'placeholder': 'First Name'}),
        }