# Generated by Django 2.0.2 on 2018-04-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quick_Requirements', '0002_auto_20180402_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quick_requirements',
            name='Quick_Requirements_Tentative_Dates',
            field=models.DateField(null=True),
        ),
    ]
