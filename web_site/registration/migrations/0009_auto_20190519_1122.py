# Generated by Django 2.2 on 2019-05-19 08:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0008_masterclass_camp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='masterclass',
            name='isAvalable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='date_end',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='date_start',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='masterclass',
            name='seats',
            field=models.PositiveSmallIntegerField(default=15),
        ),
    ]