# Generated by Django 3.2.8 on 2021-10-25 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='name',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
