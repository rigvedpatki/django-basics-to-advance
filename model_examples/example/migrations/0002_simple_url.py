# Generated by Django 2.0.4 on 2018-05-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='simple',
            name='url',
            field=models.URLField(default='www.examples.com'),
        ),
    ]
