from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog-single.html')


def services(request):
    return render(request, 'service.html')

def about(request):
    return render(request, 'about.html')


def doctor(request):
    return render(request, 'doctor.html')
