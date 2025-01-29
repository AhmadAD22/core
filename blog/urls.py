from django.urls import path
from .views import *

urlpatterns = [

path("",blogs_list,name='blogs_list'),
path("<int:id>",single_blog,name='single_blog')

    
]