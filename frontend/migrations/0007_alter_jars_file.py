# Generated by Django 5.0.4 on 2024-04-30 01:53

import frontend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_alter_jars_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jars',
            name='file',
            field=models.FileField(upload_to=frontend.models.get_upload_to),
        ),
    ]
