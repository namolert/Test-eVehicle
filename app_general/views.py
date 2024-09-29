from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from app_vehicles.models import Vehicle
from .forms import SubscriptionModelForm
from .models import Subscription

def home(request):
    return render(request, 'app_general/home.html')

def about(request):
    return render(request, 'app_general/about.html')

def subscription(request):
    if request.method == 'POST':
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('subscription_thx'))
    else:
        form = SubscriptionModelForm()
    context = {'form': form}
    return render(request, 'app_general/subscription_form.html', context)

def subscription_thx(request):
    return render(request, 'app_general/subscription_thx.html')