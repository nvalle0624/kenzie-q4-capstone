# Generated by Django 3.2.5 on 2021-07-19 15:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofilepic',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='static/profile_pics/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg'])]),
        ),
    ]
