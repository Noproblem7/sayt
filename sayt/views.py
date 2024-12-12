from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'about.html', context)

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post_list.html'
