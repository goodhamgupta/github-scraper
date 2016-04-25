from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
import json
import logging
import requests
import re
from datetime import datetime,timedelta

class LoginViewSet(viewsets.ViewSet):

    def list(self,request):
        return render(request,"scraper/login.html")


class ScraperViewSet(viewsets.ViewSet):

    def list(self,request):
        headers = {"Accept": "application/vnd.github.v3+json"}
        url = "https://www.github.com/saltstack/salt"

        #repo_name = re.search('.github.com/(.+?)/*$',url).group()
        user_repo = url.split("github.com/",1)[1]
        user = user_repo.split("/",2)[0]
        repo = user_repo.split("/",2)[1]

        r = requests.get("https://api.github.com/repos/"+str(user)+"/"+str(repo),headers=headers)

        data = r.json()
        flag=0
        if r.status_code == 200:
            logging.info("Successful")
            for key,value in data.iteritems():
                    if key == "open_issues_count":
                        issues_open = value


        one_day_back = datetime.now()-timedelta(hours=24)
        issues_24_url = "https://api.github.com/repos/"+str(user)+"/"+str(repo)+"/issues?since="+str(one_day_back)+"&per_page=10000"
        print issues_24_url
        r = requests.get(issues_24_url)
        issues_day_count = len(r.json())

        one_week_back = datetime.now()-timedelta(hours=168)
        one_week_url = issues_24_url = "https://api.github.com/repos/"+str(user)+"/"+str(repo)+"/issues?since="+str(one_week_back)+"&per_page=10000"
        r = requests.get(one_week_url,headers=headers)
        issues_week_count = len(r.json())
        return Response({"status":r.status_code,"data":{"open issues":issues_open,"1 day old":issues_day_count,"week old":issues_week_count,"Older":issues_open-issues_week_count}})