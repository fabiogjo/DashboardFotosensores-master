from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms


class Cadastro_form(ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome','sobrenome','email', 'chave_freshdesk', 'celular', 'foto', 'password')

        
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'sobrenome': forms.TextInput(attrs={'placeholder': 'Sobrenome'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'chave_freshdesk': forms.TextInput(attrs={'placeholder': 'Chave Freshdesk'}),
            'celular': forms.TextInput(attrs={'placeholder': 'Celular'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Senha'}),

        }