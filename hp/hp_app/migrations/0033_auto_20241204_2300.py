# Generated by Django 3.0 on 2024-12-04 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0032_spareparts_sparepartsize'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sparepartsize',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='sparepartsize',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
