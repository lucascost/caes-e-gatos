from django import forms

from account.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='Senha')
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','password']


class UserLoginForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email', 'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Senha', 'class':'form-control'}), label='Senha')

    class Meta:
        model = User
        fields = ['email','password']
