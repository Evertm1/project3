# Generated by Django 3.2.9 on 2022-01-29 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]