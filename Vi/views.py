from django.shortcuts import render

# Create your views here.
from Vi.models import Plans


def getViPlans(request):
    planslist = Plans.objects.all()
    print(planslist)
    return render(request,'plans.html',{'planslist':planslist})
