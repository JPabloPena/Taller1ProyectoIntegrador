# Generated by Django 3.0.6 on 2020-05-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temphum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temphum',
            name='latitud',
            field=models.CharField(default=1, max_length=20, verbose_name='Latitud'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='temphum',
            name='mes',
            field=models.CharField(default=2, max_length=20, verbose_name='Mes'),
            preserve_default=False,
        ),
    ]
