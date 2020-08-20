# Generated by Django 2.2.13 on 2020-06-24 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area_table',
            old_name='TypeOfHouse_table',
            new_name='typeOfHouse_table',
        ),
        migrations.RenameField(
            model_name='city_table',
            old_name='Province_table',
            new_name='province_table',
        ),
        migrations.RenameField(
            model_name='newhouseinfo_table',
            old_name='Area_table',
            new_name='area_table',
        ),
        migrations.RenameField(
            model_name='typeofhouse_table',
            old_name='City_table',
            new_name='city_table',
        ),
        migrations.AlterModelTable(
            name='area_table',
            table='area_table',
        ),
        migrations.AlterModelTable(
            name='city_table',
            table='city_table',
        ),
        migrations.AlterModelTable(
            name='newhouseinfo_table',
            table='newHouseInfo_table',
        ),
        migrations.AlterModelTable(
            name='province_table',
            table='province_table',
        ),
        migrations.AlterModelTable(
            name='typeofhouse_table',
            table='typeOfHouse_table',
        ),
    ]
