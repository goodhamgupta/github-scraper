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
from django.contrib import messages

from django.template import RequestContext
#class ScraperViewSet(viewsets.ViewSet):



#@login_user
@api_view(['GET'])
def search(request):
    if request.method == 'GET':
        return render(request,"search_page.html")

@api_view(['GET','POST'])
def results(request,url):

    if request.method == 'GET':
        url = request.GET.get("url")
        headers = {"Accept": "application/vnd.github.v3+json"}
        #url = request.POST.post("url")
        print "URL",url
        #repo_name = re.search('.github.com/(.+?)/*$',url).group()
        try:
            user_repo = url.split("github.com/",1)[1]
            user = user_repo.split("/",2)[0]
            repo = user_repo.split("/",2)[1]
        except:
            messages.add_message(request._request,messages.INFO,"Invalid URL/Repo does not exist")
            return redirect("/search")
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
            request.session['24hr_url'] = issues_24_url
            r = requests.get(issues_24_url,headers=headers)
            issues_day_count = len(r.json())

            one_week_back = datetime.now()-timedelta(hours=168)
            one_week_url = "https://api.github.com/repos/"+str(user)+"/"+str(repo)+"/issues?since="+str(one_week_back)+"&per_page=10000"
            request.session['one_week_url'] = one_week_url
            r = requests.get(one_week_url,headers=headers)
            issues_week_count = len(r.json())
            data = {"open_issues":issues_open,"24hr_old":issues_day_count,"week_old":issues_week_count,"older":issues_open-issues_week_count}
            print data
            return render(request,"results.html",{"data":data})
        else:
            return redirect("/search")

@api_view(['GET'])
def details(request,id):
    print id
    if int(id) == 2:
        print "inside"
        url = request.session['24hr_url']
        r = requests.get(url)
        data = r.json()
        print url
        return render(request,"list_issues.html",{"data":data})
    elif int(id) == 3:
        url = request.session['one_week_url']
        r = requests.get(url)
        data = r.json()
        return render(request,"list_issues.html",{"data":data})
    else:
        pass
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
        return redirect('/search')


def logout(request):
    if request.method == 'GET':
        #del request.session['user']
        messages.add_message(request,messages.INFO,"Logout Successful")
        return redirect("/login/")
