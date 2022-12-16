# Generated by Django 4.1 on 2022-11-30 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dnit_bi', '0027_alter_estudo_tecnico_situacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudo_tecnico',
            name='situacao',
            field=models.CharField(choices=[('Em Análise', 'Em Análise'), ('Anulado', 'Anulado'), ('Aguardando Revisão Análise', 'Aguardando Revisão Análise'), ('Aguardando Análise', 'Aguardando Análise'), ('Aguardando Ajuste Elaboração', 'Aguardando Ajuste Elaboração'), ('Em Elaboração', 'Em Elaboração'), ('Aprovado', 'Aprovado'), ('Aguardando Elaboração', 'Aguardando Elaboração')], max_length=40),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='data_criacao',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('Iluminador', 'Iluminador'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Ajuste de Display', 'Ajuste de Display'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Aferição', 'Aferição'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Ajuste Fino', 'Ajuste Fino'), ('Falha de disco', 'Falha de disco'), ('Internet', 'Internet'), ('Equipamento Offline', 'Equipamento Offline'), ('infraestrutura', 'infraestrutura'), ('Falha de Camera', 'Falha de Camera'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Enquadramento', 'Enquadramento'), ('Falha de infração', 'Falha de infração'), ('Service Task', 'Service Task'), ('OCR', 'OCR'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical'), ('Manutenção corretiva', 'Manutenção corretiva'), ('Solicitação de Análise', 'Solicitação de Análise'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('Poda / Roçada', 'Poda / Roçada'), ('Conectorização', 'Conectorização'), ('Outro', 'Outro'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acao', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('equipamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.equipamento')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
