# Generated by Django 3.2.24 on 2024-02-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registered_employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeregistrationsmodel',
            name='employeeCode',
            field=models.CharField(max_length=50),
        ),
    ]
