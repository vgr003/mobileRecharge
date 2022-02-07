from django import forms


# creating a form
class RechargeForm(forms.Form):
    phone_number = forms.CharField(max_length=200)
    operator = forms.CharField(max_length=200)
    plan = forms.IntegerField()


