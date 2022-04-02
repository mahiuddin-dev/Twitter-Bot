from django.contrib import admin

# Register your models here.
from .models import TweetPost,Following


class TweetPostAdmin(admin.ModelAdmin):
    list_display = ['tweet','schedule_post','schedule_time','schedule_date','post_done']
    list_filter = ['created_at','post_done','schedule_date']
    search_fields = ['tweet']

admin.site.register(TweetPost,TweetPostAdmin)

class FollowingAdmin(admin.ModelAdmin):
    list_display = ['user','user_id','followback']
    list_filter = ['created_at','user']
    search_fields = ['user']

admin.site.register(Following,FollowingAdmin)

