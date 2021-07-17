# Generated by Django 3.2.5 on 2021-07-17 19:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dogs', '0001_initial'),
        ('admin_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('start_time', models.TimeField(default=django.utils.timezone.now)),
                ('end_time', models.TimeField(default=django.utils.timezone.now)),
                ('start_check', models.BooleanField(default=False)),
                ('started', models.TimeField(default=django.utils.timezone.now)),
                ('ended', models.TimeField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('report_submitted', models.BooleanField(default=False)),
                ('max_slots', models.IntegerField(default=0)),
                ('slots_available', models.IntegerField(default=0, editable=False)),
                ('full', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('dogs_in_session', models.ManyToManyField(blank=True, to='dogs.Dog')),
                ('trainer', models.ManyToManyField(to='admin_users.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('notes', models.TextField()),
                ('dog_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.dog')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_sessions.session')),
            ],
        ),
    ]
