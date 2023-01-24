from django.contrib import admin
from .models import *


class OfflineAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'municipio', 'offline_desde', 'ticket',)


class Ticket_freshdeskAdmin(admin.ModelAdmin):
    list_display = ('id_ticket', 'municipio', 'tipo', 'agente',)
    search_fields = ['equipamento__numero_de_serie']


class ParalisadoAdmin(admin.ModelAdmin):
    list_display = ('faixa', 'municipio', 'data_abertura', 'data_encerramento', 'motivo', "status", "situacao",)
    search_fields = ['data_abertura', 'data_encerramento']
    list_filter = ('faixa__equipamento__ul','faixa__equipamento__municipio__lote', 'data_abertura','data_encerramento', 'status',)
    
class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('numero_de_serie', 'br', 'km', 'municipio', 'codigo', "tipo_equipamento",)
    search_fields = ['municipio__nome', 'km', 'codigo', 'numero_de_serie']
    

class Indice_desempenhoAdmin(admin.ModelAdmin):
    list_display = ('faixa', 'indice_desempenho',)
    
class SetorAdmin(admin.ModelAdmin):
    list_display = ('numero', 'responsavel',)
  
    
class AgenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'grupo', 'celular',)
    
    
class Estudo_tecnicoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'situacao', 'municipio',)
    search_fields = ['codigo']


class FaixaAdmin(admin.ModelAdmin):
    search_fields = ['equipamento__numero_de_serie']
    
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'lote', 'setor',)
    search_fields = ['nome', 'lote', 'setor']
    
class EquipamentoAnotacoesAdmin(admin.ModelAdmin):
    list_display = ('equipamento', 'anotacao', 'usuario', 'created_at',)
    search_fields = ['equipamento__numero_de_serie', 'usuario']
   
    
class NotificacaoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'equipamento', 'acao', 'created_at',)
    search_fields = ['equipamento__numero_de_serie', 'usuario']

# Register your models here.
admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Offline, OfflineAdmin)
admin.site.register(Paralisado, ParalisadoAdmin)
admin.site.register(Ticket_freshdesk, Ticket_freshdeskAdmin)
admin.site.register(Indice_desempenho, Indice_desempenhoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Agente, AgenteAdmin)
admin.site.register(Setor, SetorAdmin)
admin.site.register(Lote)
admin.site.register(EquipamentoAnotacoes, EquipamentoAnotacoesAdmin)
admin.site.register(Faixa, FaixaAdmin)
admin.site.register(Estudo_tecnico, Estudo_tecnicoAdmin)
admin.site.register(Notificacao, NotificacaoAdmin)
