from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import BlogPost
from ..forms.blog import BlogPostForm

# List View
def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/list.html', {'blogs': blogs})

#@login_required
def blog_add(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)  # إضافة request.FILES
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            messages.success(request, "تمت إضافة المقال بنجاح!")
            return redirect('blog:blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'blog/create.html', {'form': form, 'action': 'إضافة'})

@login_required
def blog_update(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog)  # إضافة request.FILES
        if form.is_valid():
            form.save()
            messages.success(request, "تم تحديث المقال بنجاح!")
            return redirect('blog:blog_list')
    else:
        form = BlogPostForm(instance=blog)
    return render(request, 'blog/update.html', {'form': form, 'action': 'تحديث'})

# Delete View
@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk, author=request.user)
    blog.delete()
    return redirect('blog:blog_list')
    