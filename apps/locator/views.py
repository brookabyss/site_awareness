import requests
import urllib2
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from .models import Site
from requests_oauthlib import OAuth1
from ..configuration import news_api,twitter_keys
from ..services import get_news,geolocator
from bs4 import BeautifulSoup
# Create your views here.

def index(request):
    source = urllib2.urlopen("https://cnn.com")
    soup = BeautifulSoup(source, 'html.parser')
    print("8   "*25)
    print(soup.get_text())
    finalList = []
    # print(geolocator("Addis Ababa"))
    return render(request,'locator/index.html')

def getNews(phrase):
    my_key=news_api['token']
    r=requests.get("https://newsapi.org/v2/everything?q="+phrase+"&apiKey="+my_key).json()
    print("*"*10)
    print("Hello get news")
    return(r)

def sendEmail(request,id):
    # # print(settings.EMAIL_HOST_USER,)
    # # current_news=getNews()
    # for art in current_news['articles']:
    #     print("source: "+art['source']['name'])
    #     print("description: "+art['description'])
    #     print("published At: " +art['publishedAt'])
    #     print("*"*50)
    # context={
    #     "articles": current_news['articles']
    # }
    send_mail(
        '',
        'Here is the message.1',
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
    return render(request,'locator/show.html')

def searchNews(request):
    if request.method=="POST":
        phrase=request.POST['phrase']
        current_news=getNews(phrase)
        context={
            "articles": current_news['articles']
        }
    return render(request,'locator/show.html',context)

def newSite(request):
    return render(request,'locator/newsite.html')

def siteDetail(request,site_id):
    s=Site.objects.get(id=site_id)
    context={
        'site':s
    }
    return render(request,'locator/site.html',context)


def createSite(request):
    if request.method=='POST':
        print(request.POST)
        sitename=request.POST['sitename']
        longitude=request.POST['longitude']
        latitude=request.POST['latitude']
        threshold=request.POST['threshold']
        email=request.POST['email']
        Site.objects.create(site_name=sitename,longitude=longitude,latitude=latitude,threshold=threshold,email=email)
        s=Site.objects.get(site_name=sitename)
        request.session['siteId']=s.id
        print("Site"*10)
        print(s,request.session['siteId'])
    return redirect(reverse('locator:site_detail',kwargs={'site_id':s.id}))


def showSites(request):
    print("site")
    sites=Site.objects.all()
    context={
    'sites':sites
    }
    return render(request,'locator/allsites.html',context)

def getTweets(request):
    context=fetchTweets()
    return render(request,'locator/all_tweets.html',context)



def fetchTweets():
    import twitter
    api = twitter.Api(consumer_key=twitter_keys['consumer_key'], consumer_secret=twitter_keys['consumer_secret'], access_token_key=twitter_keys['access_token_key'], access_token_secret=twitter_keys['access_token_secret'])
    statuses = api.GetUserTimeline("Arsenal")
    user_timeline=api.GetUserTimeline('brookfullstack')
    oAuth=OAuth1(twitter_keys['consumer_key'],twitter_keys['consumer_secret'], twitter_keys['access_token_key'],twitter_keys['access_token_secret'])
    print[s.text for s in statuses]
    # status = api.PostUpdate('Olivier Giroud!')
    searched_tweets=requests.get("https://api.twitter.com/1.1/search/tweets.json?q=mars&screen_name=@finkd",auth=oAuth).json()
    print("search"*20)

    print (searched_tweets)
    print ("query"*20)
    # sentiment=requests.get("http://text-processing.com/api/sentiment/hello").json()
    # print ("senti"*20)
    # print(sentiment)
    return({'user_timeline':user_timeline})
