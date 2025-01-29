from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import BlogPost

def home(request):
    user = request.user
    blogs=BlogPost.objects.all()[:3]
   
    return render(request, 'home.html', {'blogs': blogs})


def about(request):
    user = request.user
    blogs=BlogPost.objects.all()[:3]
   
    return render(request, 'about.html', {'blogs': blogs})