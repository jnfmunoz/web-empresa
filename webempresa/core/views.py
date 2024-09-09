from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'core/home.html')

def about(request, *args, **kwargs):
    return render(request, 'core/about.html')

def store(request, *args, **kwargs):
    return render(request, 'core/store.html')