from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', show_fasilitas_hotel, name= 'daftar_fasilitas'),
    path('tambah_fasilitas/', tambah_fasilitas, name='tambah_fasilitas'),
    # tambahkan path lainnya jika diperlukan
]
