from django.contrib import admin
from music.models import Channel
from embed_video.admin import AdminVideoMixin
from .models import Video,GameVideo,Game,Discord,feedback,Check

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Video, MyModelAdmin)
admin.site.register(GameVideo,MyModelAdmin)
admin.site.register(Game,MyModelAdmin)
admin.site.register(Discord,MyModelAdmin)
admin.site.register(feedback)
admin.site.register(Check)