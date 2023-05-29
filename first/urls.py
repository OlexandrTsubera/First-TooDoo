from django.conf.urls.static import static
from django.urls import path
from first.views import *
from django.conf import settings


urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_post/', add_post, name='add_post'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/create_comment/', create_comment, name='create_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
