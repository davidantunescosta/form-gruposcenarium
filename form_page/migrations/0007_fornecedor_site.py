# Generated by Django 5.0 on 2024-01-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_page', '0006_alter_fornecedor_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='site',
            field=models.URLField(blank=True),
        ),
    ]
