from django.shortcuts import render

# Create your views here.
from Jio.models import Plans


def getJioPlans(request):
    planslist = Plans.objects.all()
    print(planslist)
    return render(request,'plans.html',{'planslist':planslist})
