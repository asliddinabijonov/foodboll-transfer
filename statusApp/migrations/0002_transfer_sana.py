# Generated by Django 5.0.4 on 2024-04-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='sana',
            field=models.DateField(auto_now=True),
        ),
    ]
