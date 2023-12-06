from django.urls import path
from dashboard.views import show_customer, show_hotel

app_name = 'dashboard'

urlpatterns = [
    path('customer/', show_customer, name='show_customer'),
    path('hotel/', show_hotel, name='show_hotel'),
]