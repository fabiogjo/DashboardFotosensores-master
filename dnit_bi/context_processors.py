from .models import Paralisado, Offline, Equipamento, Ticket_freshdesk, Notificacao

def carrega_topbar(request):
    numero_de_paralisados = Paralisado.objects.exclude(status="Deferida (Encerramento)")
    
    numero_de_paralisados_em_acao = Paralisado.objects.exclude(status="Deferida (Encerramento)").filter(situacao="Em ação").count()
    
    numero_de_paralisados_pista_danificada = Paralisado.objects.exclude(status="Deferida (Encerramento)").filter(situacao="Pista danificada").count()
    
    numero_de_paralisados_Aguardando_autorização_diretoria_Fotosensores = Paralisado.objects.exclude(status="Deferida (Encerramento)").filter(situacao="Aguardando autorização diretoria Fotosensores").count()
    
    numero_de_paralisados_aguardando_afericao = Paralisado.objects.exclude(status="Deferida (Encerramento)").filter(situacao="Aguardando Aferição/Laudo").count()
    
    numero_de_paralisados_desparalisacao_solicitada = Paralisado.objects.exclude(status="Deferida (Encerramento)").filter(situacao="Desparalisação Solicitada").count()

    numero_de_offlines = Offline.objects.count()

    numero_de_tickets = Ticket_freshdesk.objects.all().count()
    
    notificacoes = Notificacao.objects.order_by('-created_at')[:10]
    
    

    return {

        # TOP BAR ITENS

        'numero_de_paralisados': numero_de_paralisados.count(),

        'numero_de_offlines': numero_de_offlines,

        'numero_de_tickets': numero_de_tickets,
        
        'numero_de_paralisados_em_acao': numero_de_paralisados_em_acao,
        
        'numero_de_paralisados_Aguardando_autorização_diretoria_Fotosensores': numero_de_paralisados_Aguardando_autorização_diretoria_Fotosensores,
        
        'numero_de_paralisados_aguardando_afericao': numero_de_paralisados_aguardando_afericao,
        
        'numero_de_paralisados_pista_danificada': numero_de_paralisados_pista_danificada,
        
        'numero_de_paralisados_desparalisacao_solicitada': numero_de_paralisados_desparalisacao_solicitada,
        
        'notificacoes': notificacoes
        
        

    }