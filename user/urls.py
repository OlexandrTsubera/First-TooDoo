from django.urls import path, include
from django.views.generic import TemplateView

from user.views import UserRegistrationView, Login, Logout, Profile
from user.views import confirm


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('confirm_logout/', confirm, name='confirm_logout'),
    path('profile/', Profile.as_view(), name='profile'),

]
