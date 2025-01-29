from django.urls import path,include
from .views.main import  main_dashboard
from .views.trainer import *
from .views.student import *
from .views.employee import *
from .views.blog import *

#Blog
blogpatterns=([
    path('', blog_list, name='blog_list'),
    path('add/', blog_add, name='blog_add'),
    path('update/<int:pk>/', blog_update, name='blog_update'),
    path('delete/<int:pk>/', blog_delete, name='blog_delete'),
],'blog')

# Trainer
trainerPatterns=([
    path('',trainer_list,name='trainer_list'),
    path('create',create_trainer,name='create-traner'),
    path('update/<int:id>/',update_trainer,name='update-trainer'),
    path('delete/<int:id>/',delete_trainer,name='delete_trainer'),
    path('change-password/<int:id>/',trainer_change_password,name='trainer_change_password'),


],'trainer')

# Student
studentPatterns=([
    path('',student_list,name='student_list'),
    path('create',create_student,name='create-student'),
    path('update/<int:id>/',update_student,name='update-student'),
    path('delete/<int:id>/',delete_student,name='delete_student'),
    path('change-password/<int:id>/',student_change_password,name='student_change_password'),


],'student')


managerPatterns=([
    path('',manager_list,name='manager_list'),
    path('create',create_manager,name='create-manager'),
    path('update/<int:id>/',update_manager,name='update-manager'),
    path('delete/<int:id>/',delete_manager,name='delete_manager'),
    path('change-password/<int:id>/',manager_change_password,name='manager_change_password'),


],'manager')

urlpatterns = [
    # Signup U-RL
    path('',main_dashboard, name='main_dashboard'),
    path('trainers/',include(trainerPatterns)),
    path('student/',include(studentPatterns)),
    path('employee/',include(managerPatterns)),
    path('blog/',include(blogpatterns)),
    
]