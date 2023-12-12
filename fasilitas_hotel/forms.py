from django import forms

class TambahFasilitasForm(forms.Form):
    nama_fasilitas = forms.CharField(label='Nama Fasilitas', max_length=255)
