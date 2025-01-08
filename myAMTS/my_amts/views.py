from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

def home(request):
    return render(request, 'my_amts/index.html')

def login_view(request):
    """Handle user login"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to home or dashboard
        else:
            # If authentication fails
            messages.error(request, "Invalid username or password")
    
    return render(request, 'my_amts/login.html')

def logout_view(request):
    """Handle user logout"""
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')

def signup(request):
    """Handle user signup"""
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            # Create user if passwords match
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user)  # Log the user in immediately after signup
                messages.success(request, "Sign up successful!")
                return redirect('home')
            except Exception as e:
                messages.error(request, f"Error: {e}")
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'my_amts/index.html')
