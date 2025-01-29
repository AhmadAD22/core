from django.urls import path
from django.contrib.auth import views as auth_views
from .views.auth import *
from .views.home import *
from .views.trainer import *

urlpatterns = [
    # Signup URL
    path('trainer_signup/',trainer_signup_view, name='trainer_signup'),
    path('login',login_view,name="login"),
    path('logout',logout_view,name="logout"),
    
]
