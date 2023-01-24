from datetime import datetime, timedelta
import email
from email.policy import default
from tkinter import CASCADE
from tokenize import blank_re

import requests as requests
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.db.models import Count, F, IntegerField, DateField, Min, DateTimeField, Func, Avg, DecimalField, Sum, Max, Min

# Create your models here.
from requests.auth import HTTPBasicAuth
from ckeditor.fields import RichTextField

from usuarios.models import Usuario

from django.utils import timezone


class Lote(models.Model):
    numero = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.numero}'


class Agente(models.Model):
    id_freshdesk = models.CharField(max_length=20)
    nome = models.CharField(max_length=50, null=False, blank=False)
    sobrenome = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=150, null=False, blank=False)
    grupo = models.CharField(max_length=30, null=True, blank=True)
    grupo_id = models.CharField(max_length=30, null=True, blank=True)
    celular = models.CharField(max_length=30, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'
    
    def get_setor(self):
        setor = Setor.objects.filter(responsavel=self.id)
        
        setor = setor.first()
        
        return setor


class Setor(models.Model):
    numero = models.IntegerField()
    responsavel = models.ForeignKey(Agente, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return f'Setor {self.numero}'


class Municipio(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE, null=True, blank=True)
    lote = models.ForeignKey(Lote, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.nome


class Estudo_tecnico(models.Model):
    
    SITUACAO_CHOICES = {
        
        ('Aguardando Elaboração', 'Aguardando Elaboração'),
        ('Em Elaboração', 'Em Elaboração'),
        ('Aguardando Análise', 'Aguardando Análise'),
        ('Em Análise', 'Em Análise'),
        ('Aguardando Ajuste Elaboração', 'Aguardando Ajuste Elaboração'),
        ('Aprovado', 'Aprovado'),
        ('Aguardando Revisão Análise', 'Aguardando Revisão Análise'),
        ('Anulado', 'Anulado'),

    }
    
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    codigo = models.CharField(max_length=30)
    br = models.IntegerField()
    km = models.DecimalField(decimal_places=3, max_digits=6)
    situacao = models.CharField(max_length=40, choices=SITUACAO_CHOICES, null=False, blank=False)
    ultima_atualizacao_situacao = models.DateTimeField(null=True, blank=True)
    tipo_equipamento = models.CharField(max_length=36, blank=False, null=False)
    faixas = models.CharField(max_length=36, blank=False, null=False)
    atualizado = models.DateTimeField()

    
    def __str__(self) -> str:
        return self.codigo


class Equipamento(models.Model):
    br = models.IntegerField()
    km = models.DecimalField(decimal_places=3, max_digits=6)
    codigo = models.CharField(max_length=11, blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    tipo_equipamento = models.CharField(max_length=3, blank=False, null=False)
    et = models.ForeignKey(Estudo_tecnico, on_delete=models.CASCADE, null=True, blank=True)
    ul = models.CharField(max_length=50, blank=False, null=False)
    numero_de_serie = models.IntegerField(null=True, blank=True)
    situacao_faixa = models.CharField(max_length=30, null=True)
    modo_de_operacao = models.CharField(max_length=10, null=True)
    velocidade_fiscalizada = models.IntegerField()
    velocidade_regulamentada = models.IntegerField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    estudo_tecnico_monitoramento = models.CharField(max_length=30, null=True)
    porta_velsis = models.IntegerField(null=True, blank=True)

    def __str__(self):
        serial = str(self.numero_de_serie)
        return f'{serial} - {self.municipio}'
    
    def get_faixas(self):
        faixas = Faixa.objects.filter(equipamento_id=self.id)
        return faixas
    
    def get_estado(self):
        lote = self.municipio.lote.numero
        
        if lote == 13:
            return 'SC'
        else:
            return 'RS'
  
    
    def get_data(self):
        return {
            'id': self.id,
            'lote': self.municipio.lote,
            'BR': self.BR,
            'KM': self.KM,
            'codigo': self.codigo,
            'municipio': self.municipio,
            'faixa': self.faixa,
            'tipo_equipamento': self.tipo_equipamento,
            'UL': self.UL,
            'numero_de_serie': self.numero_de_serie,
            'codigo_estudo_tecnico': self.codigo_estudo_tecnico,
            'situacao_faixa': self.situacao_faixa,
            'modo_de_operacao': self.modo_de_operacao,
            'velocidade_fiscalizada': self.velocidade_fiscalizada,
            'velocidade_regulamentada': self.velocidade_regulamentada,
            'setor': self.setor,
            'tecnico_responsavel': self.municipio.setor.reponsavel,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'estudo_tecnico_monitoramento': self.estudo_tecnico_monitoramento,

        }


    def get_indice_desempenho(self):
        
        faixas = self.get_faixas()
        
        for faixa in faixas:
        
            indice = Indice_desempenho.objects.filter(faixa_id=faixa.id).all()                         
            return indice


    def get_tickets(self):
        tickets = Ticket_freshdesk.objects.filter(equipamento_id=self.id).all().order_by('-dias_aberto').exclude(
            status="Fechado").exclude(status="Resolvido")
        return tickets
    
    
    def get_user_tickets(user):
        tickets = Ticket_freshdesk.objects.filter(agente=user).order_by('-dias_aberto').exclude(
            status="Fechado").exclude(status="Resolvido")
        return tickets


    def get_offline(self):
        offline = Offline.objects.filter(equipamento_id=self.id)
        return offline
  
    
    def get_paralisacao(self):
        
        faixas = self.get_faixas()
        
        paralisado = False
        
        for faixa in faixas:
            
            if Paralisado.objects.filter(faixa_id=faixa.id).exclude(status="Deferida (Encerramento)").exists():       
                
                paralisado = True
                
                break
                            
        return paralisado
            
    def get_coordenadas(self):
        
        return f'{self.latitude},{self.longitude}'
    
    
    def get_ultima_att_indice_atual(self):
        
        faixas = self.get_faixas()
        
        if faixas:
            lastUpdate = Indice_desempenho.objects.filter(faixa_id=faixas[0].id).values('atualizado')

            return lastUpdate[0]['atualizado']
    
    def get_paralisacao_status(self):
        faixas = self.get_faixas()
        situacao = None
        for faixa in faixas:
            status = Paralisado.objects.filter(faixa_id=faixa.id).exclude(status="Deferida (Encerramento)").first()
            if status:
                situacao = status.situacao
        
        return situacao
        
    def get_estudo_tecnico(self):
        et = Estudo_tecnico.objects.get(km=self.km)
        
        return et.codigo
    
    def get_anotacoes(self):
        
        anotacoes = EquipamentoAnotacoes.objects.filter(equipamento_id=self.id).order_by('created_at')
        
        return anotacoes
    
    def get_nova_anotacao(self):
        
        #VERIFICA SE HÁ UMA ANOTAÇÃO ADICIONADA A MENOS DE 24HRS PARA MOSTRAR NO CARD DO EQUIPAMENTO
        
        anotacao = EquipamentoAnotacoes.objects.filter(equipamento_id=self.id).order_by('-created_at')[0:1]
        
        if anotacao:
            
            anotacao = anotacao.first()

            time = timezone.now() - timedelta(hours=24) 
            
            if anotacao.created_at > time:
                
                return anotacao.usuario
            
            else:
                
                return False
        
        
        
    
    def get_offline_desde(self):
        qs = Offline.objects.filter(equipamento_id=self.id)
        
        offline = qs.first()
        
        return offline.offline_desde
    
    
    def tipos_tickets_infra_tec(self):
        
        y = False
        
        qs = Ticket_freshdesk.objects.filter(equipamento_id=self.id)  
          
        for ticket in qs:
            
            if ticket.tipo == 'Service Task' or ticket.agente == 'Monitoramento Operacional':
                
                y = True
                
        return y
            
        


class EquipamentoAnotacoes(models.Model):
    
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    anotacao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Faixa(models.Model):
    
    SENTIDO_CHOICES = {
        
        ('D', 'DECRESCENTE'),
        ('C', 'CRESCENTE')

    }
    
    
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    sentido = models.CharField(max_length=11, null=False, blank=False, choices=SENTIDO_CHOICES)
    numero = models.IntegerField()
    

    def __str__(self) -> str:
        return f'{self.equipamento.numero_de_serie} - P-{self.sentido}-{self.numero}'
    
    def get_indice_desempenho(self):
        id = Indice_desempenho.objects.filter(faixa_id=self.id)
        return id
    
    def get_paralisado(self):
        paralisacao = Paralisado.objects.filter(faixa_id=self.id).exclude(status="Deferida (Encerramento)")
        return paralisacao
    
    
class Indice_desempenho(models.Model):
    faixa = models.ForeignKey(Faixa, on_delete=models.CASCADE)
    remessas_infracoes = models.IntegerField()
    testes = models.IntegerField()
    infracoes = models.IntegerField()
    situacao = models.CharField(max_length=15)
    validas = models.IntegerField()
    invalidas = models.IntegerField()
    remessas_passagens = models.IntegerField()
    icid = models.DecimalField(max_digits=3, decimal_places=2)
    icin = models.DecimalField(max_digits=3, decimal_places=2)
    ievri = models.DecimalField(max_digits=3, decimal_places=2)
    ievdt = models.DecimalField(max_digits=3, decimal_places=2)
    ilpd = models.DecimalField(max_digits=3, decimal_places=2)
    ilpn = models.DecimalField(max_digits=3, decimal_places=2)
    icv = models.DecimalField(max_digits=3, decimal_places=2)
    ief = models.DecimalField(max_digits=3, decimal_places=2)
    periodo = models.DateField()
    dias = models.IntegerField()
    nht = models.IntegerField()
    nho = models.IntegerField()
    idf = models.DecimalField(max_digits=3, decimal_places=2)
    indice_desempenho = models.DecimalField(max_digits=3, decimal_places=2)
    atualizado = models.DateTimeField()

    # JSON
    def get_data(self):
        return {
            'serial': str(self.faixa.equipamento.numero_de_serie),
            'codigo': str(self.faixa.equipamento.codigo),
            'faixa': str(self.faixa),
            'municipio': str(self.faixa.equipamento.municipio),
            'remessas_infracoes': str(self.remessas_infracoes),
            'testes': str(self.testes),
            'infracoes': self.infracoes,
            'situacao': self.situacao,
            'validas': self.validas,
            'invalidas': self.invalidas,
            'remessas_passagens': self.remessas_passagens,
            'icid': self.icid,
            'icin': self.icid,
            'ievri': self.ievri,
            'ievdt': self.ievdt,
            'ilpd': self.ilpd,
            'ilpn': self.ilpn,
            'icv': self.icv,
            'ief': self.ief,
            'periodo': self.periodo,
            'dias': self.dias,
            'nht': self.nht,
            'nho': self.nho,
            'idf': self.idf,
            'indice_desempenho': self.indice_desempenho,
            'atualizado': self.atualizado,

        }


class Paralisado(models.Model):
    STATUS_CHOICES = (

        ("Em Análise (Início)", "Em Análise (Início)"),
        ("Em Análise (Encerramento)", "Em Análise (Encerramento)"),
        ("Deferida (Início)", "Deferida (Início)"),
        ("Deferida (Encerramento)", "Deferida (Encerramento)"),
        ("Indeferida (Início)", "Indeferida (Início)"),
        ("Indeferida (Encerramento)", "Indeferida (Encerramento)")

    )
    
    SITUACAO_CHOICES = (

        ("Em ação", "Em ação"),
        ("Pista danificada", "Pista danificada"),
        ("Aguardando autorização diretoria Fotosensores", "Aguardando autorização diretoria Fotosensores"),
        ("Aguardando Aferição/Laudo", "Aguardando Aferição/Laudo"),
        ("Desparalisação Solicitada", "Desparalisação Solicitada"),

    )

    MOTIVO_CHOICES = (

        ("Vandalismo", "Vandalismo"),
        ("Obras na Via", "Obras na Via"),
        ("Falta de Energia", "Falta de Energia"),
        ("Prazo de Validade", "Prazo de Validade"),
        ("Choque de Veículos", "Choque de Veículos"),
        ("Incidentes da Natureza", "Incidentes da Natureza"),
        ("Manutenção Corretiva", "Manutenção Corretiva"),
        ("Manutenção Preventiva", "Manutenção Preventiva"),
        ("Outro Motivo", "Outro Motivo")

    )

    faixa = models.ForeignKey(Faixa, on_delete=models.CASCADE)
    data_abertura = models.DateField()
    data_encerramento = models.DateField(null=True, blank=True)
    motivo = models.CharField(max_length=30, choices=MOTIVO_CHOICES, blank=False, null=False)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, null=False, blank=False)
    situacao = models.CharField(max_length=100, choices=SITUACAO_CHOICES, null=False, blank=False, default="Em ação")

    def __str__(self):
        r = str(self.faixa.equipamento.numero_de_serie)
        return r

    def municipio(self):
        return self.faixa.equipamento.municipio

    def get_data(self):
        return {
            'id': str(self.id),
            'lote': str(self.faixa.equipamento.municipio.lote),
            'serial': str(self.faixa.equipamento.numero_de_serie),
            'codigo': str(self.faixa.equipamento.codigo),
            'faixa': str(self.faixa),
            'municipio': str(self.faixa.equipamento.municipio),
            'data_abertura': str(self.data_abertura),
            'data_encerramento': str(self.data_encerramento) if self.data_encerramento != None else '',
            'motivo': str(self.motivo),
            'status': str(self.status)
            
            

        }


class Ticket_freshdesk(models.Model):
    TIPO_CHOICES = {

        ("Aferição", "Aferição"),
        ("Ajuste de Display", "Ajuste de Display"),
        ("Ajuste de Imagem", "Ajuste de Imagem"),
        ("Ajuste Fino", "Ajuste Fino"),
        ("Conectorização", "Conectorização"),
        ("Configuração de envio SIOR", "Configuração de envio SIOR"),
        ("Enquadramento", "Enquadramento"),
        ("Equipamento Offline", "Equipamento Offline"),
        ("Equipamento sem energia", "Equipamento sem energia"),
        ("Falha de Camera", "Falha de Camera"),
        ("Falha de disco", "Falha de disco"),
        ("Falha de infração", "Falha de infração"),
        ("Iluminador", "Iluminador"),
        ("Implantação / ajuste de sinalização", "Implantação / ajuste de sinalização"),
        ("Implantação/Reparo de sinalização horizontal", "Implantação/Reparo de sinalização horizontal"),
        ("Implantação/Reparo de sinalização vertical", "Implantação/Reparo de sinalização vertical"),
        ("infraestrutura", "infraestrutura"),
        ("Instalação / Reparo de cabo lógico", "Instalação / Reparo de cabo lógico"),
        ("Instalação / Reparo de energia eletrica", "Instalação / Reparo de energia eletrica"),
        ("Internet", "Internet"),
        ("Manutenção corretiva", "Manutenção corretiva"),
        ("Manutenção Preventiva", "Manutenção Preventiva"),
        ("OCR", "OCR"),
        ("Outro", "Outro"),
        ("PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS", "PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS"),
        ("Poda / Roçada", "Poda / Roçada"),
        ("Sem passagem / Não infracionando", "Sem passagem / Não infracionando"),
        ("Service Task", "Service Task"),
        ("Solicitação de Análise", "Solicitação de Análise"),
    }

    PRIORIDADE_CHOICES = {

        ("Baixa", "Baixa"),
        ("Media", "Media"),
        ("Alta", "Alta"),
        ("Urgente", "Urgente"),

    }

    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    id_ticket = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=100, null=True, choices=TIPO_CHOICES)
    data_criacao = models.DateField(auto_now_add=True, blank=True)
    tags = models.CharField(max_length=30, null=True, blank=True)
    dias_aberto = models.IntegerField()
    pecas = models.CharField(max_length=30, null=True, blank=True)
    prioridade = models.CharField(max_length=30, choices=PRIORIDADE_CHOICES)
    assunto = models.CharField(max_length=150)
    status = models.CharField(max_length=10)
    agente = models.CharField(max_length=100, null=True)
    descricao = RichTextField(blank=True, null=True)

    def __str__(self):
        r = str(self.id_ticket)
        return r

    def municipio(self):
        return self.equipamento.municipio

    def lote(self):
        return self.equipamento.municipio.lote

    def consulta_ticket(self):
        auth = HTTPBasicAuth('COuIBILolWo6vqXmL9R0', '')

        headers = {'Accept': 'application/json'}

        base_url = f"https://fotosensores-dnit.freshdesk.com/api/v2/tickets/{self.id_ticket}?include=conversations"

        response = requests.get(f'{base_url}', auth=auth,
                                headers=headers)

        dados = response.json()

        return dados

    def get_status(self):
        return self.status
    
    def get_assunto(self):
        
        return self.assunto


class Offline(models.Model):
    ticket = models.ForeignKey(Ticket_freshdesk, on_delete=models.CASCADE)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    offline_desde = models.DateField()
    dias_offline = models.IntegerField()

    def __str__(self):
        r = str(self.equipamento.numero_de_serie)
        return r

    def municipio(self):
        return self.equipamento.municipio


class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, null=True, blank=True)
    acao = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_data(self):
        
        return {
            'usuario': str(f'{self.usuario.nome} {self.usuario.sobrenome}' ),
            'equipamento': str(self.equipamento),
            'acao': str(self.acao),
            'created_at': str(self.created_at),

        }