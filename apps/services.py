import requests
from .configuration import news_api,twitter_keys,geo

def get_news(source):
    if source=="BBC":
        news=requests.get("https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey="+news_api['token']).json()
        return (news)


def geolocator(address):
    print("&"*10)
    # geo_info=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=Addis+Ababa&key="+geo['token']).json()
    # print geo_info
    # return geo_info
    r=requests.get("https://montanaflynn-geocoder.p.mashape.com/Seattle").json()
    print (r)
