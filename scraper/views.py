from django.shortcuts import render, redirect, render_to_response

# Create your views here.

from rest_framework import viewsets
from rest_framework.decorators import api_view
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
from django.contrib.auth import authenticate, login, logout

from django.template import RequestContext
#class ScraperViewSet(viewsets.ViewSet):

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/search')
    return redirect(request,'/login')


@api_view(['GET'])
def search(request):
    if request.method == 'GET':
        #request.session["user"] = "test"
        #print request.session["user"]
        return render(request,"search_page.html")

@api_view(['GET','POST'])
def results(request,url):

    if request.method == 'GET':
        url = request.GET.get("url")
        headers = {"Accept": "application/vnd.github.v3+json"}
        #url = request.POST.post("url")
        print "URL",url
        #repo_name = re.search('.github.com/(.+?)/*$',url).group()
        user_repo = url.split("github.com/",1)[1]
        user = user_repo.split("/",2)[0]
        repo = user_repo.split("/",2)[1]

        r = requests.get("https://api.github.com/repos/"+str(user)+"/"+str(repo),headers=headers)
        data = r.json()
        print data
        if r.status_code == 200:
            logging.info("Successful")
            for key,value in data.iteritems():
                    if key == "open_issues_count":
                        issues_open= value

        one_day_back = datetime.now()-timedelta(hours=24)
        issues_24_url = "https://api.github.com/repos/"+str(user)+"/"+str(repo)+"/issues?since="+str(one_day_back)+"&per_page=10000"
        print issues_24_url
        r = requests.get(issues_24_url)
        issues_day_count = len(r.json())

        one_week_back = datetime.now()-timedelta(hours=168)
        one_week_url = "https://api.github.com/repos/"+str(user)+"/"+str(repo)+"/issues?since="+str(one_week_back)+"&per_page=10000"
        r = requests.get(one_week_url,headers=headers)
        issues_week_count = len(r.json())
        data = {"open issues":issues_open,"24hr_old":issues_day_count,"week_old":issues_week_count,"older":issues_open-issues_week_count}
        print data
        return render(request,"results.html",{"data":data})


#class LoginViewSet(viewsets.ViewSet):
@api_view(['GET','POST'])
def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        '''
        Perform authentication here
        '''
        print "Inside"
        print request.body
        print request.data
        return redirect('/search/')
