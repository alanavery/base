# Generated by Django 3.1.5 on 2021-01-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('room_type', models.CharField(max_length=100)),
                ('beds', models.CharField(max_length=100)),
                ('accessible', models.BooleanField()),
                ('occupied', models.BooleanField()),
                ('spotless', models.BooleanField()),
            ],
        ),
    ]
