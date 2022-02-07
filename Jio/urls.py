from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.getJioPlans),
    #path('hello/', views.sayHello),

]