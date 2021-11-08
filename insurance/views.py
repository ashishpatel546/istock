from django.shortcuts import render
from mutualFund.models import Service
from insurance.models import Insurance


services = Service.objects.all()
# Create your views here.
def showtypes(request):
    insurances = Insurance.objects.all()
    data = {'services': services, 'insurances': insurances}
    return render(request, 'insurance.html', data)