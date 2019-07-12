# Generated by Django 2.2 on 2019-07-10 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0012_auto_20190601_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamCoaches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Camp')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Coach')),
            ],
        ),
    ]
