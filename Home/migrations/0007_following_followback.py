# Generated by Django 3.2 on 2022-04-02 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_following_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='followback',
            field=models.BooleanField(default=False),
        ),
    ]