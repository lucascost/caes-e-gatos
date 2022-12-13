from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.datetime_safe import date, datetime
from django.views.generic import ListView

from account.forms import UserLoginForm
from core.filters import AnuncioFilter
from core.forms import AnuncioForm
from core.models import Anuncio

# Create your views here.
def inicio(request):
    print(request.user)
    recentes = Anuncio.objects.all().order_by('-data_criacao')[:12]
    form = UserLoginForm()
    return render(request, 'index.html', {'recentes': recentes, 'form': form})

def view_anuncio(request, anuncio_id):
    pub = Anuncio.objects.get(id=anuncio_id)
    return render(request,'anuncio/detalhes.html', {'anuncio': pub})

@login_required(login_url='account:login')
def add_anuncio(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            anuncio = form.save(commit=False)
            anuncio.perfil = request.user.perfil
            anuncio.save()
            return redirect('/')

    form = AnuncioForm()
    return render(request, 'anuncio/forms/add.html', {'form': form})
@login_required(login_url='account:login')
def update_anuncio(request, anuncio_id):
    anuncio_instance = Anuncio.objects.get(id=anuncio_id)
    if request.method == 'POST':
        form = AnuncioForm(request.POST, request.FILES)
        if form.is_valid():
            img_type = str(form.cleaned_data['image'])[-3:].upper()
            permit = ['JPG', 'PEG', 'PNG']
            if img_type in permit:
                anuncio = form.save(commit=False)
                anuncio.id = anuncio_id
                anuncio.perfil = request.user.perfil
                anuncio.data_criacao = datetime.now()
                anuncio.save()
                return redirect('/')


    form = AnuncioForm(instance=anuncio_instance)
    return render(request, 'anuncio/forms/add.html', {'form': form, 'img': anuncio_instance.image.url})

def ver_todos(request):
    tipo_animal = request.GET.get('tipo_animal')
    estado = request.GET.get('estado')
    cidade = request.GET.get('cidade')
    #
    query = Anuncio.objects.all()
    print(query)
    print(f'animal: {tipo_animal}, estado: {estado}, cidade: {cidade}')

    if tipo_animal is not None and tipo_animal is not 'None' and tipo_animal is not '':
        query = query.filter(tipo_animal=tipo_animal)
        print('entrei em tipo')

    if estado is not None and estado is not 'None' and estado is not '':
        query = query.filter(perfil__estado=estado)
        print('entrei em estado')

    if cidade is not None and cidade is not 'None' and cidade is not '':
        query = query.filter(perfil__cidade=cidade)
        print('entrei em cidade')

    filter = AnuncioFilter(request.GET, queryset=query.order_by('-data_criacao'))

    anuncios = filter.qs

    paginator = Paginator(anuncios, 12)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        anuncios = paginator.page(page)
    except (EmptyPage, InvalidPage):
        anuncios = paginator.page(paginator.num_pages)

    context = {
        'anuncios': anuncios,
        'filter': filter,
        'tipo_animal': tipo_animal if tipo_animal is not None else '',
        'estado': estado if estado is not None else '',
        'cidade': cidade if cidade is not None else ''
    }
    return render(request, 'result.html',context)

def user_posts(request):
    user_id = request.user.id
    return render(request, 'user_posts.html', {'anuncios': Anuncio.objects.filter(perfil__user = user_id)})

def delete_anuncio(request, anuncio_id):
    Anuncio.objects.filter(id=anuncio_id).delete()
    return redirect('/my/')