from django import forms
from .models import Buku, Kategori

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

    def clean_judul(self):
        judul = self.cleaned_data.get('judul')
        if len(judul) < 5:
            raise forms.ValidationError("Judul buku harus lebih dari 5 karakter.")
        return judul

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = '__all__'

    def clean_nama(self):
        nama = self.cleaned_data.get('nama')
        if len(nama) < 3:
            raise forms.ValidationError("Nama kategori harus lebih dari 3 karakter.")
        return nama