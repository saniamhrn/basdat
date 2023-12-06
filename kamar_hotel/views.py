from django.shortcuts import render, redirect, HttpResponse
from utils.query import query

def show_room_list(request):
    return render(request, "room_list.html")

def tambah_kamar(request):
    return render(request, "form_tambah_kamar.html")

def tambah_fasilitas_kamar(request):
    return render(request, "form_tambah_fasilitas_kamar.html")