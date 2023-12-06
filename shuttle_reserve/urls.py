from django.urls import path
from shuttle_reserve.views import show_shuttle_reserve

app_name = 'shuttle_reserve'

urlpatterns = [
    path('', show_shuttle_reserve, name='show_shuttle_reserve'),
]