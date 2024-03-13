import bs4
import json
from django.shortcuts import render, redirect, HttpResponseRedirect
import requests
import datetime
from datetime import date
from .utils import debut_function
from .models import Video, Live, News
from requests_html import HTMLSession
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import authenticate, login, logout
from .forms import VideoUploadForm, NewsForm, LiveForm
import time


def testing(request):
    return render(request, "child1.html")


def contact(request):
    # return render(request, "contact1.html")
    return render(request, "forming1.html")


def data_entry(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            news_form = NewsForm(request.POST)
            video_form = VideoUploadForm(request.POST)
            live_form = LiveForm(request.POST)
            if 'news_submit' in request.POST:
                if news_form.is_valid():
                    news_form.save()
                    return redirect('/data_entry/')
            elif 'video_submit' in request.POST:
                if video_form.is_valid():
                    video_form.save()
                    return redirect('/data_entry/')
            elif 'live_submit' in request.POST:
                if live_form.is_valid():
                    live_form.save()
                    return redirect('/data_entry/')
        else:
            news_form = NewsForm()
            video_form = VideoUploadForm()
            live_form = LiveForm()
        return render(request, 'forming1.html',
                      {'news_form': news_form, 'video_form': video_form, 'live_form': live_form})
    else:
        return HttpResponseRedirect('/home/')


def many_video(request):
    latest = Video.objects.filter(video_type__name='latest').order_by('-video_date')
    magical = Video.objects.filter(video_type__name='magical').order_by('-video_date')
    great_innings = Video.objects.filter(video_type__name='great_innings').order_by('-video_date')
    highlights = Video.objects.filter(video_type__name='highlights').order_by('-video_date')
    enjoyable = Video.objects.filter(video_type__name='enjoyable').order_by('-video_date')
    return render(request, "many_videos1.html",
                  context={'latest': latest, 'magical': magical, 'great_innings': great_innings,
                           'highlights': highlights, 'enjoyable': enjoyable})


def live_update_delete(request):
    if request.user.is_superuser:
        items = Live.objects.all().order_by('-video_date')
        return render(request, "update_delete_live1.html", context={"items": items})
    else:
        return HttpResponseRedirect('/home/')


def delete(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            print(id)
            pi = Live.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/update_delete/')
    else:
        return HttpResponseRedirect('/home/')


def update(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            pi = Live.objects.get(pk=id)
            fm = LiveForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/update_delete/')
        else:
            pi = Live.objects.get(pk=id)
            fm = LiveForm(instance=pi)
        return render(request, "updatelive1.html", context={"live_form": fm})
    else:
        return HttpResponseRedirect('/home/')


# this is my code to fetch data from modal time complexity reduce
def videos(request):
    latest = Video.objects.filter(video_type__name='latest').order_by('-video_date')
    magical = Video.objects.filter(video_type__name='magical').order_by('-video_date')
    great_innings = Video.objects.filter(video_type__name='great_innings').order_by('-video_date')
    highlights = Video.objects.filter(video_type__name='highlights').order_by('-video_date')
    enjoyable = Video.objects.filter(video_type__name='enjoyable').order_by('-video_date')
    return render(request, "modelvideo1.html",
                  context={'latest': latest, 'magical': magical, 'great_innings': great_innings,
                           'highlights': highlights, 'enjoyable': enjoyable})


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/data_entry/')
    else:
        fm = AuthenticationForm()
    return render(request, "loginentry1.html", context={'form': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')


def news(request):
    items = News.objects.all().order_by('-date')
    return render(request, "modelnews1.html", context={"items": items})


def news_details(request, pk):
    items = News.objects.get(id=pk)
    posts_recent = News.objects.all().order_by('-date')
    return render(request, "model_news_details1.html", context={"items": items, 'posts_recent': posts_recent})


def live(request):
    items = Live.objects.all()
    return render(request, "live1.html", context={"live": items})


def live_player(request, pk, title):
    return render(request, "liveplayer1.html", context={"url": pk, "title": title})


def about(request):
    return render(request, "about1.html")


def upcoming_matches(request):
    api_key = "05f409e3d03d7d0642acbc98fbedd58c144e02dc07ac0ab1a19a70eed640a064"  # Replace with your actual API key
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=3)  # Look for matches in the next 7 days
    api_url = f"https://apiv2.api-cricket.com/cricket/?method=get_events&APIkey={api_key}&date_start={today}&date_stop={end_date}"
    response = requests.get(api_url)
    # now I write code to fetch the result of previous 3 days results this is used for latest finished matches display
    start_date = today - datetime.timedelta(days=3)  # Look for matches in the previous 3 days
    api_url2 = f"https://apiv2.api-cricket.com/cricket/?method=get_events&APIkey={api_key}&date_start={start_date}&date_stop={today}"
    response2 = requests.get(api_url2)
    latest = Video.objects.filter(video_type__name='latest').order_by('-video_date')
    highlights = Video.objects.filter(video_type__name='highlights').order_by('-video_date')
    magical = Video.objects.filter(video_type__name='magical').order_by('-video_date')
    magical1 = Video.objects.filter(video_type__name='magical').order_by('-video_date').first()
    great_innings = Video.objects.filter(video_type__name='great_innings').order_by('-video_date')
    news1 = News.objects.all().order_by('-date').first()
    news = News.objects.all().order_by('-date')

    if response.status_code == 200:
        data = response.json()
        data1 = data['result']
        data1 = sorted(data1, key=lambda x: x['event_date_start'])
        data2 = response2.json()
        data3 = data2['result']
        finished_matches = [match for match in data3 if match.get('event_status') == 'Finished']
        finished_matches = sorted(finished_matches, key=lambda x: x['event_date_start'], reverse=True)

        return render(request, 'index1.html',
                      {'matches': data1, 'matchess': finished_matches, "latest": latest, 'news1': news1, 'news': news,
                       'highlights': highlights, 'magical': magical, "magical1": magical1,
                       'great_innings': great_innings})

    # Handle the case when the request was not successful
    return render(request, 'index1.html',
                  {'matches': None, "latest": latest, 'news1': news1, 'news': news, 'magical': magical,
                   "magical1": magical1, 'great_innings': great_innings, 'highlights': highlights})


def privacy_policy(request):
    return render(request, "privacypolicy.html")


def video_player(request, pk, title):
    return render(request, "videoplayer1.html", context={"url": pk, "title": title})


def matches(request):
    # Now I write code for live matches
    today = datetime.date.today()
    api_key = "05f409e3d03d7d0642acbc98fbedd58c144e02dc07ac0ab1a19a70eed640a064"
    api_url = f"https://apiv2.api-cricket.com/?method=get_livescore&APIkey={api_key}"
    response1 = requests.get(api_url)
    data1 = response1.json()['result'] if response1.status_code == 200 and 'result' in response1.json() else None
    data1 = [entry for entry in data1 if entry.get("event_date_start") == today]

    # now I write code for upcoming matches
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=3)  # Look for matches in the next 3 days
    api_url2 = f"https://apiv2.api-cricket.com/cricket/?method=get_events&APIkey={api_key}&date_start={today}&date_stop={end_date}"
    response2 = requests.get(api_url2)
    data2 = response2.json()['result'] if response2.status_code == 200 and 'result' in response2.json() else None
    data2 = sorted(data2, key=lambda x: x['event_date_start'])

    # now I write code for finished matches
    start_date = today - datetime.timedelta(days=3)  # Look for matches in the previous 3 days
    api_url3 = f"https://apiv2.api-cricket.com/cricket/?method=get_events&APIkey={api_key}&date_start={start_date}&date_stop={today}"
    response3 = requests.get(api_url3)
    data3 = response3.json()['result'] if response3.status_code == 200 and 'result' in response3.json() else None
    finished_matches = [match for match in data3 if match.get('event_status') == 'Finished']
    finished_matches = sorted(finished_matches, key=lambda x: x['event_date_start'], reverse=True)

    return render(request, 'matches1.html', {'data1': data1, 'data2': data2, 'data3': finished_matches})


def match_details(request, pk):
    api_key = "05f409e3d03d7d0642acbc98fbedd58c144e02dc07ac0ab1a19a70eed640a064"
    api_url = f"https://apiv2.api-cricket.com/cricket/?method=get_events&APIkey={api_key}&event_key={pk}"
    response1 = requests.get(api_url)
    data4 = response1.json()['result'] if response1.status_code == 200 and 'result' in response1.json() else None
    return render(request, "match-details.html", {'data4': data4})


def standing(request, pk):
    print("standing printing", pk)
    api_key = "05f409e3d03d7d0642acbc98fbedd58c144e02dc07ac0ab1a19a70eed640a064"
    api_url = f"https://apiv2.api-cricket.com/cricket/?method=get_standings&league_key=7740&APIkey={api_key}&league_key={pk}"
    response1 = requests.get(api_url)
    data5 = response1.json()['result'][
        'total'] if response1.status_code == 200 and 'result' in response1.json() else None

    api_url = f"https://apiv2.api-cricket.com/cricket/?method=get_teams&league_key=7740&APIkey={api_key}"
    response1 = requests.get(api_url)
    data6 = response1.json()['result'] if response1.status_code == 200 and 'result' in response1.json() else None
    return render(request, "standings1.html", {'data5': data5, 'data6': data6})


def teams(request):
    return render(request, "teams1.html")


def teams_details(request, pk):
    # now I write code for upcoming matches
    api_key = "05f409e3d03d7d0642acbc98fbedd58c144e02dc07ac0ab1a19a70eed640a064"
    today = datetime.date.today()
    end_date = today + datetime.timedelta(days=3)  # Look for matches in the next 3 days
    api_url2 = f"https://apiv2.api-cricket.com/cricket/?method=get_events&APIkey={api_key}&date_start={today}&date_stop={end_date}"
    response2 = requests.get(api_url2)
    data2 = response2.json()['result'] if response2.status_code == 200 and 'result' in response2.json() else None
    data2 = sorted(data2, key=lambda x: x['event_date_start'])
    great_innings = Video.objects.filter(video_type__name='great_innings').order_by('-video_date')

    if pk == 1:
        return render(request, "teamindia1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 2:
        return render(request, "teambangladesh1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 3:
        return render(request, "teampakistan1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 4:
        return render(request, "teamsrilanka1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 5:
        return render(request, "teamaustralia1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 6:
        return render(request, "teamengland1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 7:
        return render(request, "teamsouthafrica1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 8:
        return render(request, "teamnewzealand1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 9:
        return render(request, "teamafganistan1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 10:
        return render(request, "teamwestindies1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 11:
        return render(request, "teamscotland1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 12:
        return render(request, "teamireland1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 13:
        return render(request, "teamnetharland1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 14:
        return render(request, "teamnepal1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 15:
        return render(request, "teamnamibia1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 16:
        return render(request, "teamamerica1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 17:
        return render(request, "teamoman1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 18:
        return render(request, "teampapua1.html", context={"data2": data2, "great_innings": great_innings})
    elif pk == 19:
        return render(request, "teamcanada1.html", context={"data2": data2, "great_innings": great_innings})
    else:
        return render(request, "teamuganda1.html", context={"data2": data2, "great_innings": great_innings})


def player_detail(request, pk):
    api_url = f"https://hs-consumer-api.espncricinfo.com/v1/pages/player/home?playerId={pk}"
    headers = {'User-Agent': 'YourApp/1.0'}
    response1 = requests.get(api_url, headers=headers)
    if response1.status_code == 200:
        try:
            data5 = response1.json()['player']
            # print(data5)
            data6 = response1.json()['content']['careerAverages']

            data10 = response1.json()['content']['careerAverages']['stats']
            # print(data10)
            data7 = response1.json()['content']['topRecords']
            # print(data7)
            data8 = response1.json()['content']['matches']['types']
            # print(data8)
            today = date.today()
            # Now i write code debut data
            teamA1 = "pak"
            teamA2 = "aus"
            groundA = "Ghazafi stadium"
            dateA = 55 - 2 - 23

            # test recent match
            teamB1 = "pak"
            teamB2 = "aus"
            groundB = "Ghazafi stadium"
            dateB = 55 - 2 - 23

            # ODI debut match
            teamC1 = "pak"
            teamC2 = "aus"
            groundC = "Ghazafi stadium"
            dateC = 55 - 2 - 23

            # ODI recent match
            teamD1 = "pak"
            teamD2 = "aus"
            groundD = "Ghazafi stadium"
            dateD = 55 - 2 - 23

            # T20 debut match
            teamE1 = "pak"
            teamE2 = "aus"
            groundE = "Ghazafi stadium"
            dateE = 55 - 2 - 23

            # T20 recent match
            teamF1 = "pak"
            teamF2 = "aus"
            groundF = "Ghazafi stadium"
            dateF = 55 - 2 - 23

            for a, baby in enumerate(data8):
                if a == 0:
                    for b, babe in enumerate(baby['matches']):
                        if b == 0:
                            for c, bab in enumerate(babe['events']):
                                if c == 0:
                                    groundA = bab['match']['ground']['smallName']
                                    dateA = bab['match']['startDate'][:-14]
                                    for d, ba in enumerate(bab['match']['teams']):
                                        if d == 0:
                                            teamA1 = ba['team']['slug']
                                        else:
                                            teamA2 = ba['team']['slug']
                                if c == 1:
                                    groundB = bab['match']['ground']['smallName']
                                    dateB = bab['match']['startDate'][:-14]
                                    for d, ba in enumerate(bab['match']['teams']):
                                        if d == 0:
                                            teamB1 = ba['team']['slug']
                                        else:
                                            teamB2 = ba['team']['slug']
                        # now I am writing code in second iteration for odi matches above code is test matches data
                        if b == 1:
                            for c, bab in enumerate(babe['events']):
                                if c == 0:
                                    groundC = bab['match']['ground']['smallName']
                                    dateC = bab['match']['startDate'][:-14]
                                    for d, ba in enumerate(bab['match']['teams']):
                                        if d == 0:
                                            teamC1 = ba['team']['slug']
                                        else:
                                            teamC2 = ba['team']['slug']
                                if c == 1:
                                    groundD = bab['match']['ground']['smallName']
                                    dateD = bab['match']['startDate'][:-14]
                                    for d, ba in enumerate(bab['match']['teams']):
                                        if d == 0:
                                            teamD1 = ba['team']['slug']
                                        else:
                                            teamD2 = ba['team']['slug']
                        if b == 2:
                            for c, bab in enumerate(babe['events']):
                                if c == 0:
                                    groundE = bab['match']['ground']['smallName']
                                    dateE = bab['match']['startDate'][:-14]
                                    for d, ba in enumerate(bab['match']['teams']):
                                        if d == 0:
                                            teamE1 = ba['team']['slug']
                                        else:
                                            teamE2 = ba['team']['slug']
                                if c == 1:
                                    groundF = bab['match']['ground']['smallName']
                                    dateF = bab['match']['startDate'][:-14]
                                    for d, ba in enumerate(bab['match']['teams']):
                                        if d == 0:
                                            teamF1 = ba['team']['slug']
                                        else:
                                            teamF2 = ba['team']['slug']
            list3 = [teamA1, teamA2, groundA, dateA, teamB1, teamB2, groundB, dateB, teamC1, teamC2, groundC, dateC,
                     teamD1, teamD2, groundD, dateD, teamE1, teamE2, groundE, dateE, teamF1, teamF2, groundF, dateF]
            # now I am making list of batting overall stats
            match, inning, run, bowl, hundred, fifty, six, four = 0, 0, 0, 0, 0, 0, 0, 0
            high = []
            for index, baby in enumerate(data10, start=1):
                if 1 <= index <= 3:
                    match += baby['mt']
                    inning += baby['in']
                    run += baby['rn']
                    bowl += baby['bl']
                    hundred += baby['hn']
                    fifty += baby['ft']
                    six += baby['si']
                    four += baby['fo']
                    high.append(baby['hs'])
            high = max(high)
            list1 = [match, inning, bowl, run, high, hundred, fifty, six, four]
            # print("this is list", list1)
            # now I am making list of bowling overall stats
            matchs, innings, runs, bowls, wickets, four_wicket, five_wicket = 0, 0, 0, 0, 0, 0, 0
            bests = []
            bests_innings = []
            for index, baby in enumerate(data10, start=1):
                if 7 <= index <= 9:
                    matchs += baby['mt']
                    innings += baby['in']
                    runs += baby['rn']
                    bowls += baby['bl']
                    wickets += baby['wk']
                    bests.append(baby['bbm'])
                    bests_innings.append(baby['bbi'])
                    four_wicket += baby['fwk']
                    five_wicket += baby['fw']
            filtered_values = [value for value in bests if value not in ['-', 0]]  # Filter out '-' and 0
            bests = max(filtered_values, default=None)
            filtered_values = [value for value in bests_innings if value not in ['-', 0]]  # Filter out '-' and 0
            bests_innings = max(filtered_values, default=None)
            list2 = [match, inning, runs, bowls, wickets, bests_innings, bests, four_wicket, five_wicket]
            # now I am writing code for calculating age of player
            age = today.year - data5['dateOfBirth']['year'] - (
                    (today.month, today.day) < (data5['dateOfBirth']['month'], data5['dateOfBirth']['date']))
            return render(request, "player-details1.html",
                          context={"data": data5, "data6": data6, "data7": data7, "data8": data8, "age": age,
                                   "list1": list1, "list2": list2, "list3": list3})
        except Exception as e:
            print("there here is big errors")
            print(f"Error decoding JSON: {e}")
    else:
        print(f"Error: {response1.status_code} - {response1.text}")


def stats(request):
    return render(request, "stats1.html")
