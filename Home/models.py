from django.db import models

# Create your models here.
class TweetPost(models.Model):
    tweet = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    schedule_post = models.BooleanField(default=False)
    schedule_time = models.TimeField(null=True, blank=True)
    schedule_date = models.DateField(null=True, blank=True)
    post_done = models.BooleanField(default=False)

    def __str__(self):
        return self.tweet


class Following(models.Model):
    user = models.CharField(max_length=140)
    username = models.CharField(max_length=140)
    user_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
    followback = models.BooleanField(default=False)

    def __str__(self):
        return self.user

