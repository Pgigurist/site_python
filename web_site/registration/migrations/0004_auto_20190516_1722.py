# Generated by Django 2.2 on 2019-05-16 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20190516_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
