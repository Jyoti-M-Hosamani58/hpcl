# Generated by Django 3.0 on 2024-12-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0038_auto_20241205_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocktodept',
            name='remark',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
