# Generated by Django 5.0.4 on 2024-04-30 01:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bedrock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bedrock', to='frontend.jars')),
            ],
        ),
    ]
