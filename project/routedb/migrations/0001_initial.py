# Generated by Django 3.0.1 on 2020-01-22 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import routedb.models
import utils.helper
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RasterMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=utils.helper.random_key, editable=False, max_length=12, unique=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(height_field='height', upload_to=routedb.models.map_upload_path, width_field='width')),
                ('height', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('width', models.PositiveIntegerField(blank=True, editable=False, null=True)),
                ('corners_coordinates', models.CharField(help_text='Latitude and longitude of map corners separated by commas in following order Top Left, Top right, Bottom Right, Bottom left. eg: 60.519,22.078,60.518,22.115,60.491,22.112,60.492,22.073', max_length=255, validators=[utils.validators.validate_corners_coordinates])),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maps', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'raster map',
                'verbose_name_plural': 'raster maps',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=52)),
                ('route_json', models.TextField()),
                ('start_time', models.DateTimeField(editable=False)),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('raster_map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='routedb.RasterMap')),
            ],
            options={
                'verbose_name': 'route',
                'verbose_name_plural': 'routes',
                'ordering': ['-start_time'],
            },
        ),
    ]
