from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="locator"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^/(?P<id>\d+)/email$', views.sendEmail, name='send_email'),
    url(r'^search$', views.searchNews, name='search_news'),
    url(r'^new/site$', views.newSite, name='new_site'),
    url(r'^create/site$', views.createSite, name='create_site'),
    url(r'^site/(?P<site_id>\d+)/detail$', views.siteDetail, name='site_detail'),
    url(r'^sites$', views.showSites, name='all_sites'),
    url(r'^tweets$', views.getTweets, name='search_tweets'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
