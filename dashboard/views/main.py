from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')  # Specify the URL name for your login view
def main_dashboard(request):
    user = request.user
    courses = None
    if user.is_authenticated:
        return render(request, 'main_dashboard.html', {'courses': courses})
