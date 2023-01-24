from django.urls import path

from . import views

urlpatterns = [

    path('', views.tickets_freshdesk, name='index'),

    # JSON RESPONSES
    path('tickets_por_tipo', views.tickets_por_tipo, name='tickets_por_tipo'),
    path('tickets_por_setor', views.tickets_por_setor, name='tickets_por_setor'),
    path('tickets_por_lote', views.tickets_por_lote, name='tickets_por_lote'),
    path('indice_por_tecnico', views.indice_por_tecnico, name='indice_por_tecnico'),
    path('paralisacoes_por_mes', views.paralisacoes_por_mes, name='paralisacoes_por_mes'),
    path('json_indice_desempenho', views.json_indice_desempenho, name='json_indice_desempenho'),
    path('json_faixas_por_setor', views.json_faixas_por_setor, name='json_faixas_por_setor'),
    path('json_paralisados', views.json_paralisados, name='json_paralisados'),
    path('json_equipamentos', views.json_equipamentos, name='json_equipamentos'),
    path('consulta_agente/<int:id_agente>', views.consulta_agente, name='consulta_agente'),
    path('notificacoes', views.get_notificacoes, name='notificacoes'),
    path('json_notificacoes', views.json_notificacoes, name='json_notificacoes'),

    # INTERFACES
    path('testes', views.testes, name='testes'),
    
    path('profile', views.profile, name='profile'),
    path('paralisados', views.paralisados, name='paralisados'),
    path('offlines', views.offlines, name='offlines'),
    path('tickets_freshdesk', views.tickets_freshdesk, name='tickets_freshdesk'),
    path('indice_desempenho', views.indice_desempenho, name='indice_desempenho'),
    path('upload_id', views.upload_id, name='upload_id'),
    path('upload_et', views.upload_et, name='upload_et'),
    path('upload_paralisado', views.upload_paralisados, name='upload_paralisado'),
    path('<int:equipamento_id>', views.detalhar_equipamento, name='detalhar_equipamento'),
    

    # FUNCTIONS
    path('edita_paralisados', views.edita_paralisados, name='edita_paralisados'),
    path('cria_paralisado', views.cria_paralisado, name='cria_paralisado'),
    path('cria_ticket', views.cria_ticket, name='cria_ticket'),
    path('altera_situacao_paralisado', views.altera_situacao_paralisado, name='altera_situacao_paralisado'),
    path('busca', views.busca, name='busca'),
    path('upload_agentes', views.upload_agentes, name='upload_agentes'),
    path('nova_anotacao_equipamento/<int:equipamento_id>/<int:user_id>', views.nova_anotacao_equipamento, name='nova_anotacao_equipamento'),

]
