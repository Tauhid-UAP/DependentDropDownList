# Generated by Django 2.2 on 2020-04-12 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('category', models.CharField(choices=[('Male Category 1', 'Male Category 1'), ('Male Category 2', 'Male Category 2'), ('Male Category 3', 'Male Category 3'), ('Female Category 1', 'Female Category 1'), ('Female Category 2', 'Female Category 2'), ('Female Category 3', 'Female Category 3')], max_length=20)),
            ],
        ),
    ]
