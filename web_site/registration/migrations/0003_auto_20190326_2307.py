# Generated by Django 2.1.7 on 2019-03-26 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_auto_20190323_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='user_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
