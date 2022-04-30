from django.urls import path
from .views import home_view, ch11_view

urlpatterns = [
    path('challanges/', home_view, name='challenges'),
    path('challanges/ch11/', ch11_view, name='ch11'),
]