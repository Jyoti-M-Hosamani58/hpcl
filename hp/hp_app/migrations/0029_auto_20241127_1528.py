# Generated by Django 3.0 on 2024-11-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0028_deptstock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deptstock',
            name='qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='depttodept',
            name='qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stocktodept',
            name='qty',
            field=models.IntegerField(null=True),
        ),
    ]
