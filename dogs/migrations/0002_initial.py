# Generated by Django 3.2.5 on 2021-07-19 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dogs', '0001_initial'),
        ('training_sessions', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='booked_sessions',
            field=models.ManyToManyField(blank=True, default=None, to='training_sessions.Session'),
        ),
        migrations.AddField(
            model_name='dog',
            name='no_match_dogs',
            field=models.ManyToManyField(blank=True, default=None, related_name='_dogs_dog_no_match_dogs_+', to='dogs.Dog'),
        ),
        migrations.AddField(
            model_name='dog',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.client'),
        ),
    ]
