from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Profile
from insta.models import Post
from insta.forms import CommentForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            if new_user is not None:
                login(request, new_user)
                return redirect('home')
    user_form = RegistrationForm()
    return render(request, 'users/register.html', {'user_form':user_form})

@login_required
def index(request, id):
    current_user = Profile.objects.get(id=id).user
    posts = Post.objects.filter(user=current_user)
    profile = Profile.objects.filter(user=current_user).first()
    comment_form = CommentForm()
    return render(request, 'users/index.html', {'posts':posts, 'profile':profile, 'comment_form': comment_form})

def post_user(request, id):
    post = Post.objects.get(id=id)
    user = post.user
    posts = Post.objects.filter(user=user)
    profile = Profile.objects.filter(user=user).first()
    comment_form = CommentForm()
    return render(request, 'users/index.html', {'posts': posts, 'profile':profile, 'comment_form': comment_form})

@login_required
def post_delete(request, id):
    post = Post.objects.get(id=id)
    post_user_id = post.user.profile.id
    if request.user == post.user:
        post.delete()
    return redirect('profile', id=post_user_id)