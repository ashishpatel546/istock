from django.shortcuts import render, HttpResponse
import preipo
from preipo.models import PREIPO
from mutualFund.models import Service

# Create your views here.
services = Service.objects.all()

def showipo(request):
    all_IPO= PREIPO.objects.all()
    data = {'ipoList': all_IPO, 'services': services}
    return render(request, 'list-pre-ipo.html', data)

def showIpoData(request, url):
    ipoDatas = PREIPO.objects.filter(url = url)
    print(ipoDatas)
    data = {
        'ipodatas': ipoDatas,
        'services': services
    }
    return render(request, 'about-ipo.html', data)
