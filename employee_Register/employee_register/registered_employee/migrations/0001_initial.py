# Generated by Django 3.2.24 on 2024-02-22 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeCurrentPositioinModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positionTitle', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EMployeeRegistrationsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeName', models.CharField(max_length=200)),
                ('employeeAge', models.IntegerField(max_length=2)),
                ('employeeCode', models.PositiveIntegerField(max_length=3)),
                ('employeeCurrentPosition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registered_employee.employeecurrentpositioinmodel')),
            ],
        ),
    ]
