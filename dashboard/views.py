from django.shortcuts import render

# Create your views here.
def show_customer(request):
    return render(request, "dash_cust.html")

def show_hotel(request):
    return render(request, "dash_hotel.html")