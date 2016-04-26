from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'scraper', ScraperViewSet, 'scraperviewset')
# router.register(r'login',LoginViewSet,'loginviewset')
#
# urlpatterns = router.urls
from scraper import views

urlpatterns = [
    # ex: /polls/
    url(r'^login/$', views.login, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^results(?P<url>\w{0,50})/$',views.results,name='results'),
    url(r'^logout/', views.logout, name='logout'),
    # ex: /polls/5/
    ]

