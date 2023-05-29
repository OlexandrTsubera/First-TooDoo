from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView

from first.models import *
from .forms import *


def index(request):
    model = List.objects.all()
    context = {
        'context': model,
    }
    return render(request, 'first/index.html', context)


def about(request):
    return render(request, 'first/about.html')


def show_post(request, post_id):
    post = List.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'first/show_post.html', context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    context = {
        'form': form
    }
    return render(request, 'first/add_post.html', context)


class PostDeleteView(DeleteView):
    model = List
    template_name = 'first/post_delete.html'
    success_url = reverse_lazy('home')


class PostUpdateView(UpdateView):
    model = List
    form_class = AddPostForm
    template_name = 'first/post_edit.html'
    success_url = ''


def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post_id = request.POST.get('post_id')  # Отримання post_id з форми
            comment.save()
            return redirect('post', post_id=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'first/create_comment.html', {'form': form})


