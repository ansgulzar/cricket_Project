from django.contrib import admin
from .models import Video, VideoType, News, Live


class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'video_type', 'thumbnail', 'video_url', 'video_date')
    list_filter = ('video_type', 'video_date')
    search_fields = ('title', 'video_type__name')


admin.site.register(Video, VideoAdmin)

admin.site.register(VideoType)


class Video_typeAdmin(admin.ModelAdmin):
    list_display = 'name'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'subtitle', 'para1', 'para2', 'para3', 'para4', 'para5', 'para6', 'poster', 'image1', 'image2',
        'image3', 'date')


@admin.register(Live)
class LiveAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'thumbnail', 'video_url', 'video_date')
