from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def base(request):
    return render(request, 'base.html')


def nokia(request):
    return render(request, 'nokia.html')