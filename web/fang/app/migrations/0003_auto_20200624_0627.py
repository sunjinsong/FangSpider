# Generated by Django 2.2.13 on 2020-06-24 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200624_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area_table',
            old_name='typeOfHouse_table',
            new_name='typeofhouse_table',
        ),
        migrations.AlterModelTable(
            name='newhouseinfo_table',
            table='newhouseinfo_table',
        ),
        migrations.AlterModelTable(
            name='typeofhouse_table',
            table='typeofhouse_table',
        ),
    ]