from django import forms
from .models import List, Comment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title', 'image', 'context']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
