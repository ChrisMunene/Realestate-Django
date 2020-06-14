from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from inquiries.models import Inquiry

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not first_name or not last_name or not username or not password or not confirm_password:
            messages.error(request, 'Please fill all form field to register.')
            return redirect('register')
        elif password != confirm_password :
            messages.error(request, 'Provided passwords must match')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'That username is taken.')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'That email is taken.')
            return redirect('register')
        else:
            # Register user
            user = User.objects.create_user(username=username, email=email, password=password, 
            first_name=first_name, last_name=last_name)
            auth.login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('index')
        
        
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Incorrect Username/Password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    inquiries = Inquiry.objects.order_by('-created_at').filter(user_id=request.user.id)
    context = {
        'inquiries': inquiries
    }
    return render(request, 'accounts/dashboard.html', context)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out.')
    return redirect('index')
