import django_filters
from django import forms

from core.models import Anuncio

choices = [('Gato','Gato'),('Cachorro','Cachorro')]

class AnuncioFilter(django_filters.FilterSet):
    tipo_animal = django_filters.ChoiceFilter(choices= choices, widget = forms.Select(attrs={'class':'form-select'}))
    class Meta:
        model = Anuncio
        fields = ['tipo_animal']