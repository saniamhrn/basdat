from django.urls import path
from shuttle_reserve.views import *

app_name = 'shuttle_reserve'

urlpatterns = [
    path('<int:rsv_id>/', reservasi_shuttle, name='reservasi_shuttle'),
]