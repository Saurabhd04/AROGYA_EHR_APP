# Generated by Django 3.1.1 on 2020-11-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appV1', '0002_emergencyinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalinfo',
            name='emailId',
            field=models.EmailField(max_length=50),
        ),
    ]
