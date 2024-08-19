from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .models import *
from .forms import *
# Create your views here.

@login_required
def feed(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        new_comment = comment_form.save(commit=False)
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_comment.post = post
        new_comment.save()
    else:
        comment_form = CommentForm()
    posts = Post.objects.all()
    logged_user = request.user

    return render(request, 'insta/index.html', {'posts':posts, 'logged_user':logged_user, 'comment_form':comment_form})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreateForm(data=request.GET)
    return render(request, 'insta/create_post.html', {'form':form})
