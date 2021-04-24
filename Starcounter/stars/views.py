from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import re
from django.shortcuts import redirect
from django.urls import reverse
from django.http.response import HttpResponseRedirect
# Create your views here.

def index(request):
    return HttpResponse("Go to http://127.0.0.1:8000/stars/user_name/")

def list_repos_of_a_user(request, user_name):
    url_list = []
    star_count = 0
    
    URL = f"https://api.github.com/users/{user_name}/repos?page=1"
    headers = {'accept': 'application/vnd.github.v3+json'}
    
    res = requests.get(url = URL)
    repos = res.json()

    if res.status_code == 404:
        return JsonResponse({'message': 'user not found',
        'status_code':'404'})

    while 'next' in res.links.keys():
        URL = res.links['next']['url']
        res = requests.get(url = URL)
        repos.extend(res.json())

    for repo in repos:
        url_list.append(repo['html_url'])
        star_count += repo['stargazers_count']
    
    context = {}
    context['url_list'] = url_list
    context['user_name'] = user_name
    context['star_count'] = star_count
    context['status_code'] = 200
    return JsonResponse(context)

def page_not_found(request, exception=None):
    #return HttpResponse("ni dziala")
    return HttpResponseRedirect(reverse('list_repos_of_a_user', kwargs={'user_name':'notfound'})) 