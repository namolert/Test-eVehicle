from django.contrib import admin
from app_vehicles.models import Vehicle

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_available', 'rent_end_at']
    search_fields = ['title']
    list_filter = ['is_available']

admin.site.register(Vehicle, VehicleAdmin)