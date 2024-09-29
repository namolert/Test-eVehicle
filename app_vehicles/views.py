from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Vehicle

# Create your views here.

def vehicles(request):
    all_vehicles = Vehicle.objects.order_by('is_available')
    context = {'vehicles': all_vehicles}
    return render(request, 'app_vehicles/vehicles.html', context)

def vehicle(request, vehicle_id):
    one_vehicle = None
    try:
        one_vehicle = Vehicle.objects.get(id=vehicle_id)
    except:
        print("Vehicle not found")
    context = {'vehicle': one_vehicle}
    return render(request, 'app_vehicles/vehicle.html', context)