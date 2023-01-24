from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms


class Edita_paralisado_form(ModelForm):
    class Meta:
        model = Paralisado
        fields = ('faixa', 'data_abertura', 'data_encerramento', 'motivo', 'status',)

        widgets = {
            'faixa': forms.Select(attrs={'id': 'serial', 'class': 'verified'}),
            'data_abertura': forms.DateTimeInput(attrs={'id': 'data_de_abertura', 'type': 'date', 'class': 'verified'}),
            'data_encerramento': forms.DateTimeInput(attrs={'id': 'data_de_encerramento', 'type': 'date'}),
            'motivo': forms.Select(attrs={'id': 'motivo', 'class': 'verified'}),
            'status': forms.Select(attrs={'id': 'status', 'class': 'verified'}),

        }


class Adicionar_anotacao_ticket(forms.Form):
    anotacao = forms.CharField(label='Adicionar Anotação', max_length=100)
    id_ticket = forms.IntegerField(label='Adicionar Anotação', show_hidden_initial=True)
    equipamento = forms.IntegerField(label='Adicionar Anotação', show_hidden_initial=True)


class Cria_ticket_form(ModelForm):
    class Meta:
        model = Ticket_freshdesk
        
        fields = ('equipamento', 'assunto', 'prioridade', 'tipo', 'descricao', )

        widgets = {
            'equipamento': forms.Select(attrs={'id': 'serial', 'class': 'verified'}),
            'tipo': forms.Select(attrs={'id': 'tipo', 'class': 'verified'}),

        }
        
class UploadIdForm(forms.Form):
    file  = forms.FileField()