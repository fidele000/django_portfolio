# Generated by Django 3.0.3 on 2020-02-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='about_me',
            field=models.TextField(default=''),
        ),
    ]
