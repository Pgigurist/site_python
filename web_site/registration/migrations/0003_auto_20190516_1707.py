# Generated by Django 2.2 on 2019-05-16 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Заявка', 'verbose_name_plural': 'Заявки на участие'},
        ),
        migrations.AlterModelOptions(
            name='masterclass',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курсы'},
        ),
        migrations.AlterModelOptions(
            name='userprofileinfo',
            options={'verbose_name': 'Аккаунт', 'verbose_name_plural': 'Аккаунты'},
        ),
    ]
