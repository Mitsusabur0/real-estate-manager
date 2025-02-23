# Generated by Django 5.1.4 on 2025-01-20 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management_clients', '0001_initial'),
        ('management_properties', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='current_owner',
            field=models.ForeignKey(blank=True, help_text='Current owner of the property', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='properties', to='management_clients.client'),
        ),
    ]
