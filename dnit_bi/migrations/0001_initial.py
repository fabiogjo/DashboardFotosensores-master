# Generated by Django 4.1 on 2022-08-26 14:10

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_freshdesk', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('grupo_id', models.CharField(max_length=30)),
                ('grupo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BR', models.IntegerField()),
                ('KM', models.DecimalField(decimal_places=3, max_digits=6)),
                ('codigo', models.CharField(max_length=11)),
                ('tipo_equipamento', models.CharField(max_length=3)),
                ('UL', models.CharField(max_length=50)),
                ('numero_de_serie', models.IntegerField(blank=True, null=True)),
                ('codigo_estudo_tecnico', models.CharField(max_length=30, null=True)),
                ('situacao_faixa', models.CharField(max_length=30, null=True)),
                ('modo_de_operacao', models.CharField(max_length=10, null=True)),
                ('velocidade_fiscalizada', models.IntegerField()),
                ('velocidade_regulamentada', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('estudo_tecnico_monitoramento', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentido', models.CharField(choices=[('C', 'CRESCENTE'), ('D', 'DECRESCENTE')], max_length=11)),
                ('numero', models.IntegerField()),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.equipamento')),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_freshdesk',
            fields=[
                ('id_ticket', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[('Equipamento Offline', 'Equipamento Offline'), ('PISTA DANIFICADA SEM CONDI????ES PRA REFAZER LA??OS', 'PISTA DANIFICADA SEM CONDI????ES PRA REFAZER LA??OS'), ('Configura????o de envio SIOR', 'Configura????o de envio SIOR'), ('Manuten????o corretiva', 'Manuten????o corretiva'), ('Ajuste de Display', 'Ajuste de Display'), ('Conectoriza????o', 'Conectoriza????o'), ('Ajuste Fino', 'Ajuste Fino'), ('Sem passagem / N??o infracionando', 'Sem passagem / N??o infracionando'), ('Solicita????o de An??lise', 'Solicita????o de An??lise'), ('Ajuste de Imagem', 'Ajuste de Imagem'), ('Enquadramento', 'Enquadramento'), ('Equipamento sem energia', 'Equipamento sem energia'), ('Implanta????o / ajuste de sinaliza????o', 'Implanta????o / ajuste de sinaliza????o'), ('Manuten????o Preventiva', 'Manuten????o Preventiva'), ('Instala????o / Reparo de cabo l??gico', 'Instala????o / Reparo de cabo l??gico'), ('Iluminador', 'Iluminador'), ('Outro', 'Outro'), ('Falha de Camera', 'Falha de Camera'), ('Falha de disco', 'Falha de disco'), ('Aferi????o', 'Aferi????o'), ('Internet', 'Internet'), ('Instala????o / Reparo de energia eletrica', 'Instala????o / Reparo de energia eletrica'), ('infraestrutura', 'infraestrutura'), ('OCR', 'OCR'), ('Implanta????o/Reparo de sinaliza????o horizontal', 'Implanta????o/Reparo de sinaliza????o horizontal'), ('Poda / Ro??ada', 'Poda / Ro??ada'), ('Implanta????o/Reparo de sinaliza????o vertical', 'Implanta????o/Reparo de sinaliza????o vertical'), ('Falha de infra????o', 'Falha de infra????o')], max_length=100, null=True)),
                ('data_criacao', models.DateField(blank=True, default=datetime.datetime.now)),
                ('tags', models.CharField(blank=True, max_length=30, null=True)),
                ('dias_aberto', models.IntegerField()),
                ('pecas', models.CharField(blank=True, max_length=30, null=True)),
                ('prioridade', models.CharField(choices=[('Media', 'Media'), ('Baixa', 'Baixa'), ('Alta', 'Alta'), ('Urgente', 'Urgente')], max_length=30)),
                ('assunto', models.CharField(max_length=150)),
                ('status', models.CharField(max_length=10)),
                ('agente', models.CharField(max_length=100, null=True)),
                ('descricao', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.equipamento')),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.agente')),
            ],
        ),
        migrations.CreateModel(
            name='Paralisado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_abertura', models.DateField()),
                ('data_encerramento', models.DateField(blank=True, null=True)),
                ('motivo', models.CharField(choices=[('Vandalismo', 'Vandalismo'), ('Obras na Via', 'Obras na Via'), ('Falta de Energia', 'Falta de Energia'), ('Prazo de Validade', 'Prazo de Validade'), ('Choque de Ve??culos', 'Choque de Ve??culos'), ('Incidentes da Natureza', 'Incidentes da Natureza'), ('Manuten????o Corretiva', 'Manuten????o Corretiva'), ('Manuten????o Preventiva', 'Manuten????o Preventiva'), ('Outro Motivo', 'Outro Motivo')], max_length=30)),
                ('status', models.CharField(choices=[('Em An??lise (In??cio)', 'Em An??lise (In??cio)'), ('Em An??lise (Encerramento)', 'Em An??lise (Encerramento)'), ('Deferida (In??cio)', 'Deferida (In??cio)'), ('Deferida (Encerramento)', 'Deferida (Encerramento)'), ('Indeferida (In??cio)', 'Indeferida (In??cio)'), ('Indeferida (Encerramento)', 'Indeferida (Encerramento)')], max_length=30)),
                ('faixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.faixa')),
            ],
        ),
        migrations.CreateModel(
            name='Offline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offline_desde', models.DateField()),
                ('dias_offline', models.IntegerField()),
                ('equipamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.equipamento')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.ticket_freshdesk')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.lote')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.setor')),
            ],
        ),
        migrations.CreateModel(
            name='Indice_desempenho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remessas_infracoes', models.IntegerField()),
                ('testes', models.IntegerField()),
                ('infracoes', models.IntegerField()),
                ('situacao', models.CharField(max_length=15)),
                ('validas', models.IntegerField()),
                ('invalidas', models.IntegerField()),
                ('remessas_passagens', models.IntegerField()),
                ('icid', models.DecimalField(decimal_places=2, max_digits=3)),
                ('icin', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ievri', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ievdt', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ilpd', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ilpn', models.DecimalField(decimal_places=2, max_digits=3)),
                ('icv', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ief', models.DecimalField(decimal_places=2, max_digits=3)),
                ('periodo', models.DateField()),
                ('dias', models.IntegerField()),
                ('nht', models.IntegerField()),
                ('nho', models.IntegerField()),
                ('idf', models.DecimalField(decimal_places=2, max_digits=3)),
                ('indice_desempenho', models.DecimalField(decimal_places=2, max_digits=3)),
                ('atualizado', models.DateTimeField()),
                ('faixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.faixa')),
            ],
        ),
        migrations.AddField(
            model_name='equipamento',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dnit_bi.municipio'),
        ),
    ]
