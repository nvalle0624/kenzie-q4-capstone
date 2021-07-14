# Generated by Django 3.2.5 on 2021-07-14 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('email', models.EmailField(max_length=254)),
                ('cert', models.CharField(blank=True, max_length=50)),
                ('field_of_expertise', models.CharField(choices=[('Trainer', 'Trainer'), ('Walker', 'Walker'), ('Hiker', 'Hiker'), ('Runner', 'Runner'), ('Behaviorist', 'Behaviorist')], max_length=11)),
                ('admin_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
