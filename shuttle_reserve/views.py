from django.shortcuts import render

# Create your views here.
def show_shuttle_reserve(request):
    return render(request, "shuttle_reserve.html")