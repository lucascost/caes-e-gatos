from django.urls import path
from core import views

app_name='core'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('anuncios/', views.ver_todos, name='ver_todos'),
    path('anuncios/v/<int:anuncio_id>', views.view_anuncio, name='ver_anuncio'),
    path('add/', views.add_anuncio, name='add_anuncio'),
    path('edit/<int:anuncio_id>', views.update_anuncio, name='edit_anuncio'),
    path('delete/<int:anuncio_id>', views.delete_anuncio, name='delete_anuncio'),
    path('my/', views.user_posts, name='user_posts')
]