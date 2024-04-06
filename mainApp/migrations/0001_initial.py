# Generated by Django 5.0.4 on 2024-04-04 06:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Davlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Davlatlar',
            },
        ),
        migrations.CreateModel(
            name='Pozitsiya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('turi', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name_plural': 'pozitsiya',
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='clublar/')),
                ('prezident', models.CharField(blank=True, max_length=255, null=True)),
                ('trener', models.CharField(max_length=255)),
                ('t_sana', models.DateField(blank=True, null=True)),
                ('kapital', models.PositiveIntegerField(blank=True, null=True)),
                ('davlat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.davlat')),
            ],
            options={
                'verbose_name_plural': 'Clublar',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=255)),
                ('son', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('t_sana', models.DateField(blank=True, null=True)),
                ('maosh', models.PositiveIntegerField(blank=True, null=True)),
                ('narx', models.PositiveIntegerField(blank=True, null=True)),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.club')),
                ('davlat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.davlat')),
                ('pozitsiya', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.pozitsiya')),
            ],
            options={
                'verbose_name_plural': 'Playerlar',
            },
        ),
    ]