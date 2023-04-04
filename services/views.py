from django.shortcuts import render


def home(request):
    return render(request, 'services/pages/index.html')

def about(request):
    pass

def services(request):
    return render(request, 'services/pages/services.html')

def pages(request):
    pass

def contact(request):
    return render(request, 'services/pages/contact.html')

