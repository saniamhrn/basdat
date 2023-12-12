from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', show_daftar_hotel, name='daftar_hotel'),
    path('detail-hotel/<str:nib>/', detail_hotel, name='detail_hotel'),
    # Add more URLs for room creation, updating, etc.
]