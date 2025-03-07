"""
URL configuration for blog application.
"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_page, name='blog-page'),
    path('posts/', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail-page'),  #/post/my-first-post
]
