from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('recharge/', views.recharge),
    path('op-finder/', views.operatorFinder),

]