# Generated by Django 2.2 on 2019-05-16 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_masterclass_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masterclass',
            name='seats',
            field=models.PositiveSmallIntegerField(default=50),
        ),
    ]
