from django.shortcuts import render
from .models import Service

# Create your views here.
def services(request, *args, **kwargs):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services' : services})