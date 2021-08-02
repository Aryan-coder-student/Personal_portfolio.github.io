from django.shortcuts import render , redirect
from music.models import Channel,Video,GameVideo,Game,Discord,feedback,Check
from googleapiclient.discovery import build
import requests
from django.conf import settings
from isodate import parse_duration
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
search_url = 'https://www.googleapis.com/youtube/v3/search'
vid_url='https://www.googleapis.com/youtube/v3/videos'
def homepage(request):
    if request.method == 'POST':
        b = Check.objects.all()[0]
        ps_check = request.POST.get("passwords")
        print(ps_check)
        if ps_check == b.password:
            return render(request,"college.html")
        else :
            messages.warning(request, 'Wrong Password')
    return render(request,"menu.html")




def mymusic(request):
    return render(request,"mymusic.html")




def lecture(request):
    ch = Channel.objects.all()
    context ={"ytch":ch }
    return render(request,"Lectures.html",context)




def favchannel(request):
    all_chanel=Channel.objects.all()
    return render(request,"ytchannel.html")





def ourmember(request):
    if request.method=="POST":
        username1 = request.POST.get("name")
        desc1 = request.POST.get("subject")        
        x = feedback.objects.create(name=username1, feedback_desc=desc1)
        x.save()
        return render(request,"email.html")  
    return render(request,"email.html")



def college(request):
    return render(request,"college.html")






def python(request):
    vi = Video.objects.all()
    conte ={"vide": vi}
    return render(request,"python.html",conte)


def game(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    vid_url='https://www.googleapis.com/youtube/v3/videos'
    gvi = Game.objects.all()
    
    
    search_param = {"parts" : 'snippet' , 'q' : 'python tutorials' , 'maxResults' : 10 ,'key':settings.YOUTUBE_DATA_API_KEY , 'type':'video'}
    r = requests.get(search_url, params=search_param)
    vi_id=[]
    
    gv= GameVideo.objects.all()
    
    result =r.json()['items']
    
    for a in result:
        y = a['id']['videoId']
        vi_id.append(y)
    print(vi_id)
    
    video_param={"part" : 'snippet,contentDetails','key':settings.YOUTUBE_DATA_API_KEY , 'id' : ','.join(vi_id)}
    r = requests.get(vid_url,params=video_param)
    video_result=r.json()['items']
    video_title=[]
    
    video_thumbnail=[]
    detail = []
    for v in video_result:
        video_item={
            'date' :v['snippet']['publishedAt'],
            'time':parse_duration(v['contentDetails']['duration']),
            'id':"https://www.youtube.com/watch?v="+v['id'],
            'title':v['snippet']['title'],
            'thumbnails':v['snippet']['thumbnails']['high']['url'],

        }
        detail.append(video_item)
    contents ={"ytgv": gv,'detail': detail , 'gvi':gvi}

    return render(request,"game.html",contents)





def discord(request):
    search_params= {"parts" : 'snippet' , 'q' : 'discord python tutorial' , 'maxResults' : 10 ,'key':settings.YOUTUBE_DATA_API_KEY , 'type':'video'}
    rrr = requests.get(search_url, params=search_params)
    vi_ids=[]
    results =rrr.json()['items']

    for aa in results:
        yy = aa['id']['videoId']
        vi_ids.append(yy)
    video_params={"part" : 'snippet,contentDetails','key':settings.YOUTUBE_DATA_API_KEY , 'id' : ','.join(vi_ids)}
    rr = requests.get(vid_url,params=video_params)
    video_results=rr.json()['items']
    details = []
    for v in video_results:
        video_items={
            'dates' :v['snippet']['publishedAt'],
            'times':parse_duration(v['contentDetails']['duration']),
            'ids':"https://www.youtube.com/watch?v="+v['id'],
            'titles':v['snippet']['title'],
            'thumbnail':v['snippet']['thumbnails']['high']['url'],
        }
        details.append(video_items)
    dis = Discord.objects.all()
    context = {'details': details , "disc" : dis}
    return render(request,"discord.html",context)








