from rest_framework import serializers
from .models import Kategori, Buku

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'