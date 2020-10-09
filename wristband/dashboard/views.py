from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def maps_google(request):
    return render(request, 'dashboard/map-google.html')