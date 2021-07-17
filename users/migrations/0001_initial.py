# Generated by Django 3.2.5 on 2021-07-17 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('phone_contact', phone_field.models.PhoneField(blank=True, help_text='Contact Number', max_length=31)),
                ('dogs_owned', models.ManyToManyField(blank=True, to='dogs.Dog')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
