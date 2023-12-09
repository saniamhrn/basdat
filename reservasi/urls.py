from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', reservasi, name='reservasi'),
    path('daftar_reservasi_kamar', show_reservasi_kamar, name='daftar_reservasi_kamar'),
    path('detail_reservasi/<int:rsv_id>/', detail_reservasi, name='detail_reservasi'),
    
    
    # Add more URLs for room creation, updating, etc.
]