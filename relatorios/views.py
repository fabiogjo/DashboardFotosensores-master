from django.shortcuts import render
from relatorios.models import *
from django.http import JsonResponse

def index(request):
    
    relatorio_ticket = Relatorio_ticket.objects.all()
    
    context = {
        
        'relatorio_ticket': relatorio_ticket
        
    }
    
    return render(request, 'relatorios/index.html', context)




def solved_tickets(request):
    tickets = Relatorio_ticket.objects.all()
    data = [ticket.get_data() for ticket in tickets]
    response = {'data': data}
    return JsonResponse(response)

def get_all_tickets(request):
    indices = Ticket_freshdesk.objects.all()
    data = [indice.get_data() for indice in indices]
    response = {'data': data}
    return JsonResponse(response)