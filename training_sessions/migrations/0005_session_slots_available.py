# Generated by Django 3.2.5 on 2021-07-15 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_sessions', '0004_auto_20210714_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='slots_available',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
