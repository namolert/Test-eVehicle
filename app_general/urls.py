from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('subscription', views.subscription, name='subscription'),
    path('subscription/thx', views.subscription_thx, name='subscription_thx'),
]