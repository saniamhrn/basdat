from django.shortcuts import render, redirect
from .models import Fasilitas
from .forms import TambahFasilitasForm

def show_fasilitas_hotel(request):
    # Ambil semua fasilitas dari database
    fasilitas_list = Fasilitas.objects.all()

    context = {
        'fasilitas_list': fasilitas_list,
    }

    return render(request, "daftar_fasilitas.html",context)

def tambah_fasilitas(request):
    if request.method == 'POST':
        form = TambahFasilitasForm(request.POST)
        if form.is_valid():
            nama_fasilitas = form.cleaned_data['nama_fasilitas']
            Fasilitas.objects.create(nama=nama_fasilitas)
            return redirect('daftar_fasilitas')
    else:
        form = TambahFasilitasForm()

    context = {
        'form': form,
    }
    return render(request, 'tambah_fasilitas.html', context)
