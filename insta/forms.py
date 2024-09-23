from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = ('body',)
        widgets = {
            'body': forms.TextInput(attrs={'class':'commentText', 'placeholder': 'Add to a comment...'})
        }