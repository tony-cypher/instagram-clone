from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import *
from .forms import *
from users.models import Profile
# Create your views here.

@login_required
def feed(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post = get_object_or_404(Post, id=request.POST.get('post_id'))
        user = User.objects.get(id=request.POST.get('userId'))
        if user and content:
            comment = Comment.objects.create(post=post, posted_by=user, body=content)
            return JsonResponse({'user': comment.posted_by.username, 'content': comment.body, 'created_at': comment.created}, status=201)
    comment_form = CommentForm()
    posts = Post.objects.all()
    logged_user = request.user
    users = Profile.objects.all()

    return render(request, 'insta/index.html', {'posts':posts, 'logged_user':logged_user, 'comment_form':comment_form, 'users': users})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('home')
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, 'insta/create_post.html', {'form':form})
