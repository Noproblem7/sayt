from django.contrib import admin
from django.urls import path, include
from .views import home, PostListView

urlpatterns = [
    path('', home, name='home'),
    path('posts/', PostListView.as_view(), name='posts'),

]
