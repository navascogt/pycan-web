# Generated by Django 2.1.4 on 2019-02-13 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('member_until', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('rest_address', models.CharField(blank=True, max_length=100)),
                ('po_box', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]