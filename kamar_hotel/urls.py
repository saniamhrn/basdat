from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', show_room_list, name='daftar_kamar'),
    path('tambah-kamar', tambah_kamar, name='tambah_kamar'),
    path('tambah-fasilitas-kamar', tambah_fasilitas_kamar, name='tambah_fasilitas_kamar'),

    # Add more URLs for room creation, updating, etc.
]