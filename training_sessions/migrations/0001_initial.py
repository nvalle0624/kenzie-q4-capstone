

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_users', '0001_initial'),
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=50)),
                ('time_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('time_ended', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed', models.BooleanField(default=False)),
                ('notes', models.TextField(blank=True)),
                ('dogs_in_session', models.ManyToManyField(to='dogs.Dog')),
                ('trainer', models.ManyToManyField(to='admin_users.Trainer')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('notes', models.TextField(blank=True)),
                ('dog_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.dog')),
                ('sessions', models.ManyToManyField(to='training_sessions.Session')),
            ],
        ),
    ]
