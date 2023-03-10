# Generated by Django 4.1 on 2022-09-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0013_alter_agente_grupo_alter_agente_grupo_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='prioridade',
            field=models.CharField(choices=[('Media', 'Media'), ('Urgente', 'Urgente'), ('Alta', 'Alta'), ('Baixa', 'Baixa')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('OCR', 'OCR'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Manutenção corretiva', 'Manutenção corretiva'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Ajuste de Display', 'Ajuste de Display'), ('Falha de infração', 'Falha de infração'), ('Falha de disco', 'Falha de disco'), ('Service Task', 'Service Task'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Solicitação de Análise', 'Solicitação de Análise'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Conectorização', 'Conectorização'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Equipamento Offline', 'Equipamento Offline'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('Poda / Roçada', 'Poda / Roçada'), ('Iluminador', 'Iluminador'), ('Falha de Camera', 'Falha de Camera'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Ajuste Fino', 'Ajuste Fino'), ('Internet', 'Internet'), ('infraestrutura', 'infraestrutura'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico'), ('Enquadramento', 'Enquadramento'), ('Aferição', 'Aferição'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Outro', 'Outro')], max_length=100, null=True),
        ),
    ]
