from django.db import models
from dnit_bi.models import Ticket_freshdesk, Paralisado

# Create your models here.
class Relatorio_ticket(models.Model):
    
    ticket = models.ForeignKey(Ticket_freshdesk, on_delete=models.CASCADE)
    mes = models.CharField(max_length=10)
    
    def get_grupo(self):
        if self.ticket.agente == 'Adilson Rodrigues':
            
            grupo = 'Infraestrutura'
        
        elif self.ticket.agente == 'Monitoramento Operacional':
            grupo = 'Monitoramento Operacional'
            
        else:
            grupo = 'Técnicos'
            
        return grupo
    
    def get_data(self):
        return {
            'id_ticket': str(self.ticket.id_ticket),
            'assunto': str(self.ticket.assunto).upper(),
            'grupo': self.get_grupo(),
            'data_criacao': str(self.ticket.data_criacao),
            'agente': str(self.ticket.agente),        
        }

    

class Relatorio_paralisado(models.Model):
    
    paralicao = models.ForeignKey(Paralisado, on_delete=models.CASCADE)
    mes = models.IntegerField()