# Generated by Django 3.2 on 2022-04-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_following_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
