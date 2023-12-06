from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', show_daftar_reservasi, name='daftar_reservasi'),
    path('update-reservation/<str:rsv_id>/', update_status_reservasi, name='update_reservation'),
    path('update-pembayaran/<str:rsv_id>/', update_pembayaran, name='update_pembayaran'),
    path('detail-reservation/<str:rsv_id>/', detail_reservation, name='detail_reservation'),
    # Add more URLs for room creation, updating, etc.
]