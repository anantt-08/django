# Generated by Django 3.0.5 on 2021-05-17 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_portal_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='Users',
        ),
    ]