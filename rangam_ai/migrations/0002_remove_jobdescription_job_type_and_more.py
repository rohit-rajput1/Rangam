# Generated by Django 5.0.6 on 2024-06-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rangam_ai', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobdescription',
            name='job_type',
        ),
        migrations.AlterField(
            model_name='jobdescription',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
