from datetime import datetime

from django.shortcuts import render
from django.http import HttpRequest

import Airtel.models
import Jio
import Vi
from OperatorUtility.models import OperatorDetails
from Users.forms import RechargeForm
def recharge(request):
    phone = ""
    op = ""
    plan = ""
    error_message = ""
    success = False
    tno = ""
    if request.method == 'POST':
        phone = request.POST.get("phone")
        op = operatorFinder(phone)
        operator = request.POST.get("operator")
        if str(op) != str(operator):
            error_message = "Invalid Operator!"
        plan = request.POST.get("plan")
        if len(error_message) == 0 and not(checkPlan(operator,plan)):
            error_message = "Invalid plan!"
        if len(error_message)<=0:
            success = True
            tno = getTransactionId()
    print(request.POST)
    context = {'phone':phone,
               'plan':plan,
               'operator':op,
               'error':error_message,
               'success':success,
               'transaction_id':tno,
               }
    return render(request,'recharge.html',context)

def operatorFinder(number):
   series = number[0:4]
   operator = OperatorDetails.objects.get(series = series)
   return operator

def checkPlan(operator,amount):
    isAvailable = False
    if operator == 'Airtel':
        plan = Airtel.models.Plans.objects.get(amount = amount)
        if plan:
            isAvailable = True
    if operator == 'Jio':
        plan = Jio.models.Plans.objects.get(amount = amount)
        if plan:
            isAvailable = True
    if operator == 'Vi':
        plan = Vi.models.Plans.objects.get(amount = amount)
        if plan:
            isAvailable = True

    return isAvailable
transactionNumber = 1
def getTransactionId():
    global transactionNumber
    time = datetime.now()
    tId = str(time)+str(transactionNumber)
    transactionNumber+=1
    return tId




