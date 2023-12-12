from django.db import models

class Fasilitas(models.Model):
    nomor = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return self.nama
