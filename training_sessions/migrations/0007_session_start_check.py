# Generated by Django 3.2.5 on 2021-07-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_sessions', '0006_auto_20210715_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='start_check',
            field=models.BooleanField(default=False),
        ),
    ]
