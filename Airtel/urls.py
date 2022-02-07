from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.getAirtelPlans),
    #path('hello/', views.sayHello),

]