# Generated by Django 3.0 on 2024-11-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hp_app', '0014_auto_20241125_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='Itemname',
            new_name='machineName',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='branchname',
            new_name='manufacturerName',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='description',
            new_name='receivedBy',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='part_no',
            new_name='sparePart',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='qty',
            new_name='vendorCompany',
        ),
        migrations.RenameField(
            model_name='stock',
            old_name='price',
            new_name='vendorName',
        ),
        migrations.AddField(
            model_name='stock',
            name='balanceqty',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='entryId',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='issuedqty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
        migrations.AddField(
            model_name='stock',
            name='po',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='rate',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='sparePartNo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
