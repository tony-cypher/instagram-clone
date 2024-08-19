from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'caption', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'caption': forms.Textarea(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment
        fields = ('body', 'posted_by',)
        widgets = {
            'body': forms.TextInput(attrs={'class':'form-control'})
        }