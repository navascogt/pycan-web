# Generated by Django 2.2.7 on 2019-12-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_auto_20191201_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='fee_amount',
            field=models.IntegerField(choices=[(20, 'General'), (10, 'Estudiante y/o Desempleado'), (0, 'Exento')], default=20),
        ),
    ]
