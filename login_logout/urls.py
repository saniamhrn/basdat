from django.urls import path
from login_logout.views import *

app_name = 'login_logout'

urlpatterns = [
    path('login/', login, name='login'),
    path('', logout, name='logout'),
    path("register/", register, name="register"),
    path("register/admin/", register_admin, name="register_admin"),
    path("register/customer/", register_customer, name="register_customer"),
    path("register/hotel/", register_hotel, name="register_hotel"),

]