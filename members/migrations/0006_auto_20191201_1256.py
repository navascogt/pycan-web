# Generated by Django 2.2.7 on 2019-12-01 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20191201_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='position',
            field=models.IntegerField(choices=[('PRE', 'Presidencia'), ('VPR', 'Vicepresidencia'), ('SEC', 'Secretaría'), ('TRE', 'Tesorería'), ('CH1', 'Vocalía 1'), ('CH2', 'Vocalía 2'), ('CH3', 'Vocalía 3'), ('CH4', 'Vocalía 4')]),
        ),
    ]
