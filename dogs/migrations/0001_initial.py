# Generated by Django 3.2.5 on 2021-07-07 18:39

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('breed', models.CharField(max_length=40)),
                ('age_years', models.IntegerField(default=0)),
                ('age_months', models.IntegerField(default=0)),
                ('vet_name', models.CharField(max_length=30)),
                ('vet_number', phone_field.models.PhoneField(blank=True, help_text='Contact Number', max_length=31)),
                ('vet_address', models.CharField(max_length=200)),
                ('special_needs', models.TextField()),
                ('extra_notes', models.TextField()),
                ('no_match_dogs', models.ManyToManyField(related_name='_dogs_dog_no_match_dogs_+', to='dogs.Dog')),
            ],
        ),
    ]
