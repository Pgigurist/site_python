# Generated by Django 2.2 on 2019-07-12 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_mediaimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='mediaImage',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='registration.MediaImage'),
        ),
    ]
