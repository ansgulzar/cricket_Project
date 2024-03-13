# Generated by Django 4.2.7 on 2024-01-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cricketlive', '0007_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Live',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('thumbnail', models.URLField(blank=True)),
                ('video_url', models.URLField(blank=True)),
                ('video_date', models.DateTimeField(blank=True)),
            ],
        ),
    ]
