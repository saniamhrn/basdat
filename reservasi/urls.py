from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', reservasi, name='reservasi'),
    path('daftar_reservasi_kamar', show_reservasi_kamar, name='daftar_reservasi_kamar'),
    path('detail_reservasi/<int:rsv_id>/', detail_reservasi, name='detail_reservasi'),
    path('cancel_reservasi/<int:rsv_id>/', cancel_reservasi, name='cancel_reservasi'),
    path('complaint/<int:rsv_id>/', complaint_page, name='complaint_page'),
    path('save_complaint/', save_complaint, name='save_complaint'),
    
    # Add more URLs for room creation, updating, etc.
]