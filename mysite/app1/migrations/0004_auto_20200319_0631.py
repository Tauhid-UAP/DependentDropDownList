# Generated by Django 2.2 on 2020-03-19 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200317_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='category',
            field=models.CharField(choices=[('Male Category 1', 'Male Category 1'), ('Male Category 2', 'Male Category 2'), ('Female Category 1', 'Female Category 1'), ('Female Category 2', 'Female Category 2')], max_length=20),
        ),
    ]
