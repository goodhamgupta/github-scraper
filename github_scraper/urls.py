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
    # ex: /polls/5/
    ]

