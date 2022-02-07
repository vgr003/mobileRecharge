from django.shortcuts import render
from django.http import HttpResponse

from Airtel.models import Plans


def getAirtelPlans(request):
    planslist = Plans.objects.all()
    print(planslist)
    return render(request,'plans.html',{'planslist':planslist})
