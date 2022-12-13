import django_filters
from django import forms

from core.models import Anuncio

class AnuncioFilter(django_filters.FilterSet):
    class Meta:
        model = Anuncio
        fields = ['tipo_animal']