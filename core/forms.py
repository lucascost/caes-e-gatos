from django import forms

from core.models import Anuncio, Perfil

CHOICES = [(None, None), ('Gato', 'Gato'), ('Cachorro', 'Cachorro')]

class PerfilForm(forms.ModelForm):
    estado = forms.CharField(widget=forms.Select)
    cidade = forms.CharField(widget=forms.Select)
    class Meta:
        model = Perfil
        fields = ['telefone','estado','cidade', 'bairro']

class AnuncioForm(forms.ModelForm):
    tipo_animal = forms.ChoiceField(choices=CHOICES, required=True)
    image = forms.FileField(required=True, widget=forms.FileInput(attrs={"accept": "image/png, image/jpeg"}))

    class Meta:
        model = Anuncio
        fields = ['titulo','tipo_animal','descricao', 'image']