# Generated by Django 2.2.6 on 2019-10-13 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='standupparticipation',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='standupparticipation',
            name='single_use_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
