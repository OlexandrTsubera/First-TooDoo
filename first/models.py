from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import redirect
from django.urls import reverse


class List(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="photo/%Y/%m/%d/")
    context = models.TextField(max_length=250)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Заняття'
        verbose_name_plural = 'Заняття'


class Comment(models.Model):
    post = models.ForeignKey(List, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
