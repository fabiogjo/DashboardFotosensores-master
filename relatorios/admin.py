from django.contrib import admin
from .models import *

# Register your models here.
class Relatorio_ticketAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'mes',)
    search_fields = ['ticket', 'mes']

admin.site.register(Relatorio_ticket, Relatorio_ticketAdmin)