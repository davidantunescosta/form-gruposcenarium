# Generated by Django 5.0 on 2024-01-05 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_page', '0003_alter_fornecedor_tempo_atividade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='ramo',
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='tempo_atividade',
            field=models.CharField(choices=[('opcao0', 'Selecione'), ('opcao1', 'até 2 anos'), ('opcao2', '02 à 05 anos'), ('opcao3', '05 à 10 anos'), ('opcao4', '+10 anos')], default='opcao0', max_length=100),
        ),
    ]
