from django import forms
from django.db.models.base import Model
from app_vehicles.models import Vehicle
from .models import Subscription

class VehicleMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title
    
class SubscriptionModelForm(forms.ModelForm):
    vehicle_set = VehicleMultipleChoiceField(
        queryset=Vehicle.objects.order_by('is_available'),
        required=True,
        label="Suggested Vehicle",
        widget=forms.CheckboxSelectMultiple,
    )
    accepted = forms.BooleanField(
        required=True, 
        label="sjlvns lskdk jj ps dj s mknnn"
    )

    class Meta:
        model = Subscription
        fields = ['name', 'email', 'vehicle_set', 'accepted']
        labels = {
            'name': 'Name-Surname',
            'email': 'Email',
            'vehicle_set': 'Suggested Vehicle'
        }