# Generated by Django 5.1.6 on 2025-03-06 22:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_company_tenant'),
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant'),
        ),
        migrations.AlterField(
            model_name='company',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant'),
        ),
        migrations.DeleteModel(
            name='Domain',
        ),
        migrations.DeleteModel(
            name='Tenant',
        ),
    ]
