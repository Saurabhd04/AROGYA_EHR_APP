# Generated by Django 3.0.8 on 2020-11-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appV1', '0010_auto_20201117_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptioninfo',
            name='symptoms',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
