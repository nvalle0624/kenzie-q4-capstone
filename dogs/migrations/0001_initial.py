

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
                ('age_years', models.PositiveSmallIntegerField(default=0)),
                ('age_months', models.PositiveSmallIntegerField(default=0)),
                ('vet_name', models.CharField(max_length=30)),
                ('vet_number', phone_field.models.PhoneField(blank=True, help_text='Contact Number', max_length=31)),
                ('vet_address', models.CharField(max_length=200)),
                ('special_needs', models.TextField(blank=True)),
                ('extra_notes', models.TextField(blank=True)),

            ],
        ),
    ]
