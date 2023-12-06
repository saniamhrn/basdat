from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', reservasi, name='reservasi'),
    
    # Add more URLs for room creation, updating, etc.
]