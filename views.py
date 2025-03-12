from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .serializers import KategoriSerializer, BukuSerializer
from .models import Kategori, Buku
from .forms import BukuForm, KategoriForm # type: ignore

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer

def home(request):
    query = request.GET.get('q')
    sort_by = request.GET.get('sort', 'id')  # Default sorting by 'id'
    if query:
        buku_list = Buku.objects.filter(judul__icontains=query).order_by(sort_by)
    else:
        buku_list = Buku.objects.all().order_by(sort_by)
    paginator = Paginator(buku_list, 5) # 5 Buku per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'buku_app/home.html', {'page_obj': page_obj, 'query': query, 'sort_by': sort_by})

def tambah_buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BukuForm()
    return render(request, 'buku_app/tambah_buku.html', {'form': form})

def edit_buku(request, id):
    buku = get_object_or_404(Buku, id=id)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BukuForm(instance=buku)
    return render(request, 'buku_app/edit_buku.html', {'form': form})

def daftar_kategori(request):
    kategori_list = Kategori.objects.all()
    return render(request, 'buku_app/daftar_kategori.html', {'kategori_list': kategori_list})

def tambah_kategori(request):
    if request.method == 'POST':
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_kategori')
    else:
        form = KategoriForm()
    return render(request, 'buku_app/tambah_kategori.html', {'form': form})

def edit_kategori(request, id):
    kategori = get_object_or_404(Kategori, id=id)
    if request.method == 'POST':
        form = KategoriForm(request.POST, instance=kategori)
        if form.is_valid():
            form.save()
            return redirect('daftar_kategori')
    else:
        form = KategoriForm(instance=kategori)
    return render(request, 'buku_app/edit_kategori.html', {'form': form})

def hapus_buku(request, id):
    buku = get_object_or_404(Buku, id=id)
    buku.delete()
    return redirect('home')

def hapus_kategori(request, id):
    kategori = get_object_or_404(Kategori, id=id)
    kategori.delete()
    return redirect('daftar_kategori')

