# Generated by Django 2.2.13 on 2022-08-06 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiser', '0015_auto_20220806_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organiser',
            name='mobile_no',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
