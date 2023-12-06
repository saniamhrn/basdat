from django.shortcuts import render, redirect, HttpResponse
from utils.query import query

def reservasi(request):
    return render(request, "form_reservasi.html")