# Generated by Django 3.2.5 on 2021-07-15 15:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=140)),
                ('time_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('send_to', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, related_name='send_to', to=settings.AUTH_USER_MODEL)),
                ('sent_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
