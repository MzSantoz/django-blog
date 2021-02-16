from django.shortcuts import render
from .models import Post

def hello_blog(request):
  
  post_list = Post.objects.all()
  
  data = { 
    'posts': post_list 
    }

  return render(request, 'index.html', data)