from django.shortcuts import render

# Create your views here.

def home_view(req):
    tst = 'TEST STRING'
    return render(req, 'home.html', {'tst': tst})


def ch11_view(req):
    return render(req, 'ch11.html')
