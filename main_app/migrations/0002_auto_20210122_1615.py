# Generated by Django 3.1.5 on 2021-01-22 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='online_account',
            field=models.BooleanField(default=False),
        ),
    ]
