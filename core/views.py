from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView

from account.forms import UserLoginForm
from core.filters import AnuncioFilter
from core.forms import AnuncioForm
from core.models import Anuncio

# Create your views here.
def inicio(request):
    recentes = Anuncio.objects.all().order_by('-data_criacao')[:12]
    form = UserLoginForm()
    return render(request, 'index.html', {'recentes': recentes, 'form': form})

def anuncio(request, anuncio_id):
    pub = Anuncio.objects.get(id=anuncio_id)
    return render(request,'anuncio/detalhes.html', {'anuncio': pub})

@login_required(login_url='account:login')
def add_anuncio(request):
    print(request.user)
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            anuncio = form.save(commit=False)
            anuncio.perfil = request.user.perfil
            anuncio.save()
            return redirect('/')
    form = AnuncioForm()
    return render(request, 'anuncio/forms/add.html', {'form': form})

def ver_todos(request):
    filter_key = request.GET.get('tipo_animal')
    if filter_key is not None and filter_key is not '':
        filter = AnuncioFilter(request.GET, queryset=Anuncio.objects.filter(tipo_animal=filter_key).order_by('-data_criacao'))
    else:
        filter = AnuncioFilter(request.GET, queryset=Anuncio.objects.all().order_by('-data_criacao'))
        filter_key = ''
        anuncios = filter.qs

    paginator = Paginator(anuncios, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        anuncios = paginator.page(page)
    except (EmptyPage, InvalidPage):
        anuncios = paginator.page(paginator.num_pages)

    return render(request, 'result.html',{'anuncios': anuncios, 'filter': filter, 'filter_key': filter_key})