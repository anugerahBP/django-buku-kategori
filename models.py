from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=200)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    penulis = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul