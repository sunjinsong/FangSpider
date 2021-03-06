# Generated by Django 2.2.13 on 2020-06-24 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(max_length=100)),
                ('area_url', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'Area_table',
            },
        ),
        migrations.CreateModel(
            name='City_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=100)),
                ('city_url', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'City_table',
            },
        ),
        migrations.CreateModel(
            name='Province_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Province_table',
            },
        ),
        migrations.CreateModel(
            name='TypeOfHouse_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_type', models.CharField(max_length=100)),
                ('house_url', models.CharField(max_length=500)),
                ('City_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.City_table')),
            ],
            options={
                'db_table': 'TypeOfHouse_table',
            },
        ),
        migrations.CreateModel(
            name='NewHouseInfo_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_image', models.CharField(max_length=500)),
                ('house_detail', models.CharField(max_length=200)),
                ('house_name', models.CharField(max_length=100)),
                ('house_descript', models.CharField(max_length=200)),
                ('house_size', models.CharField(max_length=100)),
                ('house_address', models.CharField(max_length=100)),
                ('house_phone', models.CharField(max_length=500)),
                ('house_price', models.CharField(default='0', max_length=50)),
                ('house_label', models.CharField(default='无', max_length=200)),
                ('Area_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Area_table')),
            ],
            options={
                'db_table': 'NewHouseInfo_table',
            },
        ),
        migrations.AddField(
            model_name='city_table',
            name='Province_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Province_table'),
        ),
        migrations.AddField(
            model_name='area_table',
            name='TypeOfHouse_table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TypeOfHouse_table'),
        ),
    ]
