from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('<str:hotel_name>/', menambah_review, name='menambah_review')
]