from django.shortcuts import render

# Create your views here.

def home_view(req):
    return render(req, 'home.html')


def ch11_view(req):
    return render(req, 'ch11.html')
