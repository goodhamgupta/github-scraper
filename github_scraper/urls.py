from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from scraper.views import *
router = DefaultRouter()
router.register(r'scraper', ScraperViewSet, 'scraperviewset')
router.register(r'login',LoginViewSet,'loginviewset')

urlpatterns = router.urls



