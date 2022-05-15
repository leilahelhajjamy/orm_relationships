# Generated by Django 4.0.4 on 2022-05-10 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbvApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='firstName',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='lastName',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='testScore',
            field=models.FloatField(default=0.0),
        ),
    ]