# Generated by Django 2.2.10 on 2021-06-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0002_auto_20210531_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticekind',
            name='days',
            field=models.IntegerField(default=0, help_text='Margen de días antes o después de la fecha de referencia'),
        ),
    ]
