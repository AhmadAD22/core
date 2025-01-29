from django.db import models
from accounts.models import User
from django.utils.text import slugify
import os

class BlogPost(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    image=models.ImageField(upload_to='blogs',null=True,blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        if self.image:
            image_path = self.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
        super().delete(*args, **kwargs)
    
    