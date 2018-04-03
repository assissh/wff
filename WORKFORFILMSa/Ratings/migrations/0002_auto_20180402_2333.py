# Generated by Django 2.0.2 on 2018-04-03 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ratings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='create_date',
            new_name='Rating_Create_Date',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='modified_date',
            new_name='Rating_Modified_Date',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='User_ID',
            new_name='Rating_User_ID',
        ),
        migrations.AddField(
            model_name='rating',
            name='Rating_Creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rate', to=settings.AUTH_USER_MODEL),
        ),
    ]