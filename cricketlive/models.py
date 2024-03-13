from django.db import models


class VideoType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Video(models.Model):
    video_type = models.ForeignKey(VideoType, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, null=False, blank=True)
    thumbnail = models.URLField(null=False, blank=True)
    video_url = models.URLField(null=False, blank=True)
    video_date = models.DateField(null=False, blank=True)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=250, null=False, blank=True)
    subtitle = models.CharField(max_length=250, null=False, blank=True)
    image1 = models.URLField(blank=True)
    image2 = models.URLField(blank=True)
    image3 = models.URLField(blank=True)
    poster = models.URLField(null=False, blank=True)
    para1 = models.TextField(null=False, blank=True)
    para2 = models.TextField(null=False, blank=True)
    para3 = models.TextField(null=False, blank=True)
    para4 = models.TextField(null=False, blank=True)
    para5 = models.TextField(null=False, blank=True)
    para6 = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Live(models.Model):
    title = models.CharField(max_length=250, null=False, blank=True)
    thumbnail = models.URLField(null=False, blank=True)
    video_url = models.URLField(null=False, blank=True)
    video_date = models.DateField(null=False, blank=True)

    def __str__(self):
        return self.title
