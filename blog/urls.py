from django.urls import path
from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    BlogPostCreateView,
    BlogPostDetailView,
    BlogPostListView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('posts/', BlogPostCreateView.as_view(), name='create_post'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('posts/list/', BlogPostListView.as_view(), name='post_list'),
]
