# Generated by Django 2.2.3 on 2019-08-22 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190822_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(default='User', max_length=15),
        ),
    ]
