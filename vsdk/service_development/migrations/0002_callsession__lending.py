# Generated by Django 2.0.4 on 2019-05-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_development', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='callsession',
            name='_lending',
            field=models.BooleanField(default=True),
        ),
    ]
