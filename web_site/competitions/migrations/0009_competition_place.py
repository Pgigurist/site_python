# Generated by Django 2.2 on 2019-06-02 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0008_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='place',
            field=models.OneToOneField(blank=True, default='1', on_delete=django.db.models.deletion.CASCADE, to='competitions.Place'),
            preserve_default=False,
        ),
    ]