# Generated by Django 2.1.7 on 2019-03-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20190326_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='group_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
