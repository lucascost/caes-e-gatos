# Generated by Django 4.1.3 on 2022-11-06 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_perfil_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]