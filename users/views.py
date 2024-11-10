from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import HealthMetrics
import matplotlib.pyplot as plt
import plotly.express as px
from django.shortcuts import redirect
from django.contrib.auth import logout

# User registration and login views
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('health_data')
    return render(request, 'users/login.html')


# Data input view
def health_data(request):
    if request.method == 'POST':
        blood_pressure = request.POST['blood_pressure']
        glucose_level = request.POST['glucose_level']
        health_entry = HealthMetrics(user=request.user, blood_pressure=blood_pressure, glucose_level=glucose_level)
        health_entry.save()
        return redirect('health_data')
    
    data = HealthMetrics.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'health_data.html', {'data': data})

# Data visualization page
def data_visualization(request):
    data = HealthMetrics.objects.filter(user=request.user).order_by('-timestamp')
    
    # Prepare visualization data
    blood_pressure_data = [entry.blood_pressure for entry in data]
    glucose_level_data = [entry.glucose_level for entry in data]
    
    # Matplotlib plot example
    fig, ax = plt.subplots()
    ax.plot(blood_pressure_data, label='Blood Pressure')
    ax.plot(glucose_level_data, label='Glucose Level')
    ax.set_title('Health Data over Time')
    ax.legend()

    # Save plot to file
    fig.savefig('/path/to/save/plot.png')

    # Plotly interactive chart example
    fig = px.line(x=list(range(len(blood_pressure_data))), y=blood_pressure_data, title='Blood Pressure Trend')
    fig.show()

    return render(request, 'visualization.html', {'plot': '/path/to/save/plot.png'})

def logout_view(request):
    logout(request)
    return redirect('home')  # Or any page you want to redirect the user to after logout


def health_data_view(request):
    return render(request, 'health_data/health_data.html')
