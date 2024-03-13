"""
URL configuration for Cricketlove project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cricketlive import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from cricketlive.forms import Loginform

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upcoming_matches, name="home"),  # $it is used for upcoming matches page
    path('about/', views.about, name="about"),  # $it is used for upcoming matches page
    path('match/', views.matches, name="match"),  # $it is used for complete matches page
    path('details/<int:pk>/', views.match_details, name="details"),  # $it is used for matches details page
    path('standing/<int:pk>/', views.standing, name="standing"),  # $it is used for Standing page
    path('teams/', views.teams, name="teams"),  # $it is used for team page
    path('teams_details/<int:pk>/', views.teams_details, name="teams_details"),  # $it is used for team details page
    path('player_details/<int:pk>/', views.player_detail, name="player_details"),  # $it is used for player details page
    path('stats/', views.stats, name="stats"),  # $it is used for Stats page
    path('live/', views.live, name="live"),  # $it is used for live page
    path('videoplayer/<path:pk>/<str:title>/', views.video_player, name="videoplayer"),  # $it is used for videoplayer of video
    path('news/', views.news, name="news"),  # $it is used for news page
    path('news_details/<int:pk>/', views.news_details, name="news_details"),
    path('loginview/', views.user_login, name='loginview'),  # $it is used for login page
    path('logoutview/', views.user_logout, name='logoutview'),  # $it is used for logout page
    path('videos/', views.videos, name='videos'),  # $it is used for all categories video page
    path('data_entry/', views.data_entry, name='data_entry'),  # $this is Data entry form url
    path('liveplayer/<path:pk>/<str:title>/', views.live_player, name='liveplayer'),  # $it is used for live match player page
    path('update_delete/', views.live_update_delete, name='update_delete'),  # $it is used for update delete live page
    path('delete/<int:id>', views.delete, name='delete'),  # $it is used for deleting any match in live page
    path('update/<int:id>', views.update, name='update'),  # $it is used for updating any match in live page
    path('manyvideos/', views.many_video, name='manyvideos'),  # $it is used for ALl many video page
    path('contact/', views.contact, name='contact'),  # $it is used for contact page
    path('testing/', views.testing, name='testing'),  # $it is used for testing
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
