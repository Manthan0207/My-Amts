from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Bus

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

def bus_list(request):
    buses = Bus.objects.all()

    # Prepare data for the map
    bus_data = []
    for bus in buses:
        for stop in bus.stops:  # Assuming stops is a JSON array with coordinates
            bus_data.append({
                "bus_no": bus.bus_number,
                "stop_name": stop.get("name"),
                "order": stop.get("order"),
                "coordinates": stop.get("coordinates"),
            })
    
    print(bus_data)

    return render(request, "my_amts/load.html", {"bus_data":bus_data})

def search_bus(request):
    """
    A view that allows a user to search for a bus by its bus_number.
    If the bus is found, it displays all its stops.
    """
    context = {}
    
    if request.method == "POST":
        # Get the bus number from the form
        bus_no = request.POST.get('bus_no')
        
        try:
            # Query the Bus model to find the bus with that number
            bus = Bus.objects.get(bus_number=bus_no)
            context['bus'] = bus
            context['stops'] = bus.stops  # This will be the list of stops from the JSONField
        except Bus.DoesNotExist:
            # If no bus found, set an error message in the context
            context['error'] = f"Bus with number {bus_no} does not exist."
    
    return render(request, 'my_amts/search_bus.html', context)
