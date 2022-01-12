# Generated by Django 2.2.4 on 2022-01-12 08:12

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SkateboardParks',
            fields=[
                ('ogc_fid', models.AutoField(primary_key=True, serialize=False)),
                ('park_id', models.IntegerField(blank=True, null=True)),
                ('facilityid', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('name_fr', models.CharField(blank=True, max_length=80, null=True)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('address_fr', models.CharField(blank=True, max_length=80, null=True)),
                ('facility_t', models.CharField(blank=True, max_length=80, null=True)),
                ('facility_1', models.CharField(blank=True, max_length=80, null=True)),
                ('accessctrl', models.CharField(blank=True, max_length=80, null=True)),
                ('accessible', models.CharField(blank=True, max_length=80, null=True)),
                ('open', models.CharField(blank=True, max_length=80, null=True)),
                ('notes', models.CharField(blank=True, max_length=80, null=True)),
                ('modified_d', models.DateField(blank=True, null=True)),
                ('created_da', models.DateField(blank=True, null=True)),
                ('facility', models.CharField(blank=True, max_length=80, null=True)),
                ('facility_f', models.CharField(blank=True, max_length=80, null=True)),
                ('descriptio', models.CharField(blank=True, max_length=80, null=True)),
                ('descript_1', models.CharField(blank=True, max_length=80, null=True)),
                ('picture_li', models.CharField(blank=True, max_length=80, null=True)),
                ('picture_de', models.CharField(blank=True, max_length=80, null=True)),
                ('picture_1', models.CharField(blank=True, db_column='picture__1', max_length=80, null=True)),
                ('wkb_geometry', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
            options={
                'db_table': 'skateboard_parks',
                'managed': False,
            },
        ),
    ]
