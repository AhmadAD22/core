from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from .models import BlogPost

def blogs_list(request):
    query = request.GET.get("query", "")  # الحصول على كلمة البحث من الطلب
    if query:
        blogs = BlogPost.objects.filter(title__icontains=query)  # البحث عن المقالات التي تحتوي على النص
    else:
        blogs = BlogPost.objects.all()  
        
    paginator = Paginator(blogs, 9)  # Show 9 blogs per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the relevant page object
    return render(request, 'blogs/blogs_list.html', {'page_obj': page_obj,"query": query,})

def single_blog(request,id):
    blog = get_object_or_404(BlogPost,id=id)
    return render(request, 'blogs/single_blog.html', {'blog': blog})