from django.urls import path

from core import views

app_name='core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('anuncios/', views.ver_todos, name='ver_todos'),
    path('anuncios/v/<int:anuncio_id>', views.anuncio, name='ver_anuncio'),
    path('add/', views.add_anuncio, name='add_anuncio'),

]