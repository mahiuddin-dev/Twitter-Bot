# Generated by Django 3.2 on 2022-03-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetpost',
            name='tweet',
            field=models.TextField(max_length=140),
        ),
    ]