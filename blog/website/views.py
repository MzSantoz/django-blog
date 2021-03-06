from django.shortcuts import render
from .models import Post, Contact

def blog(request):
  
  post_list = Post.objects.filter(deleted=False)
  
  data = { 
    'posts': post_list 
    }

  return render(request, 'index.html', data)

def post_detail(request, slug):
  post = Post.objects.get(slug = slug)
  return render(request, 'post_detail.html', {'post':post})

def send_message(request):
  name = request.POST['name']
  Contact.objects.create(
    name = name,
    email = request.POST['email'],
    message = request.POST['message']
  )
  return render(request, 'message_sent.html', {'contact_name': name})