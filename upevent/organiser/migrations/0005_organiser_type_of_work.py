# Generated by Django 2.2.13 on 2022-07-29 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0004_organiser'),
    ]

    operations = [
        migrations.AddField(
            model_name='organiser',
            name='type_of_work',
            field=models.CharField(choices=[('FOOD', 'FOOD'), ('DECORATION', 'DECORATION'), ('MUSIC', 'MUSIC'), ('LIGHTING', 'LIGHTING'), ('STAGE PROGRAM', 'STAGE PROGRAM')], default='MUSIC', max_length=30),
        ),
    ]