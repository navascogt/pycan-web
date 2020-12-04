# Generated by Django 2.2.10 on 2020-11-25 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0023_feed_roles'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='role',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='members.Role'),
        ),
    ]