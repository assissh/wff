# Generated by Django 2.0.2 on 2018-03-31 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_Qna_Comment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='HelpQna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Help_Qna_Answer', models.CharField(max_length=100)),
                ('Help_Qna_Article_Id', models.IntegerField()),
                ('Help_Qna_Question', models.CharField(max_length=100)),
                ('Help_Qna_Modified_Date', models.DateField(auto_now_add=True)),
                ('Help_Qna_Created_Date', models.DateField(auto_now_add=True)),
                ('Help_Qna_Creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='helpqna', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='Comment_Help_Qna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='help_Qna.HelpQna'),
        ),
        migrations.AddField(
            model_name='comment',
            name='Help_Qna_Comment_Author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentqna', to=settings.AUTH_USER_MODEL),
        ),
    ]
