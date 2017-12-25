import requests
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, reverse
from requests_oauthlib import OAuth1
from ..configuration import news_api
from bs4 import BeautifulSoup

def get_news(source):

    if source=="BBC":
        news=requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey="+news_api['token']).json()
        print (news)

def index(request):
    print("news app"*20)
    # get_news('BBC')
    # do whatever with bs to populate the list
    return render(request,'news/all_news.html')
