from django.shortcuts import render
from .models import Post

def blog(request):
  
  post_list = Post.objects.filter(deleted=False)
  
  data = { 
    'posts': post_list 
    }

  return render(request, 'index.html', data)