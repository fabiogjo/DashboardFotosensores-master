# Generated by Django 4.1 on 2022-11-10 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnit_bi', '0024_alter_estudo_tecnico_situacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudo_tecnico',
            name='situacao',
            field=models.CharField(choices=[('Aprovado', 'Aprovado'), ('Anulado', 'Anulado'), ('Aguardando Revisão Análise', 'Aguardando Revisão Análise'), ('Aguardando Análise', 'Aguardando Análise'), ('Em Elaboração', 'Em Elaboração'), ('Aguardando Ajuste Elaboração', 'Aguardando Ajuste Elaboração'), ('Em Análise', 'Em Análise'), ('Aguardando Elaboração', 'Aguardando Elaboração')], max_length=40),
        ),
        migrations.AlterField(
            model_name='faixa',
            name='sentido',
            field=models.CharField(choices=[('C', 'CRESCENTE'), ('D', 'DECRESCENTE')], max_length=11),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='prioridade',
            field=models.CharField(choices=[('Urgente', 'Urgente'), ('Baixa', 'Baixa'), ('Media', 'Media'), ('Alta', 'Alta')], max_length=30),
        ),
        migrations.AlterField(
            model_name='ticket_freshdesk',
            name='tipo',
            field=models.CharField(choices=[('Falha de disco', 'Falha de disco'), ('Falha de Camera', 'Falha de Camera'), ('Outro', 'Outro'), ('PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS', 'PISTA DANIFICADA SEM CONDIÇÕES PRA REFAZER LAÇOS'), ('Configuração de envio SIOR', 'Configuração de envio SIOR'), ('Instalação / Reparo de cabo lógico', 'Instalação / Reparo de cabo lógico'), ('Aferição', 'Aferição'), ('Solicitação de Análise', 'Solicitação de Análise'), ('infraestrutura', 'infraestrutura'), ('Internet', 'Internet'), ('Poda / Roçada', 'Poda / Roçada'), ('Sem passagem / Não infracionando', 'Sem passagem / Não infracionando'), ('Ajuste Fino', 'Ajuste Fino'), ('Conectorização', 'Conectorização'), ('Manutenção Preventiva', 'Manutenção Preventiva'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Equipamento Offline', 'Equipamento Offline'), ('Implantação/Reparo de sinalização horizontal', 'Implantação/Reparo de sinalização horizontal'), ('Service Task', 'Service Task'), ('Falha de infração', 'Falha de infração'), ('Implantação / ajuste de sinalização', 'Implantação / ajuste de sinalização'), ('OCR', 'OCR'), ('Ajuste de Display', 'Ajuste de Display'), ('Instalação / Reparo de energia eletrica', 'Instalação / Reparo de energia eletrica'), ('Manutenção corretiva', 'Manutenção corretiva'), ('Iluminador', 'Iluminador'), ('Enquadramento', 'Enquadramento'), ('Implantação/Reparo de sinalização vertical', 'Implantação/Reparo de sinalização vertical')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='EquipamentoAnotacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anotacao', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.equipamento')),
            ],
        ),
    ]
