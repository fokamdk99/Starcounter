from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import re
from django.shortcuts import redirect
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.views import View
# Create your views here.
class Git_handler(View):
    http_method_names = ['get']
    def dispatch(self, request, *args, **kwargs):
        URL = f"https://api.github.com/users/{self.kwargs['user_name']}/repos?page=1"
        headers = {'accept': 'application/vnd.github.v3+json'}
        
        res = requests.get(url = URL)
        self.status_code = res.status_code
        repos = res.json()
        self.message = 'user found'
        if res.text == '[]':
            self.message = 'user not found'
    
        while 'next' in res.links.keys():
            URL = res.links['next']['url']
            res = requests.get(url = URL)
            repos.extend(res.json())

        self.repos = repos
        self.user_name = self.kwargs['user_name']
        self.url_list = self.list_repositories()
        self.star_count = self.count_stars()
        return super(Git_handler, self).dispatch(request, *args, **kwargs)
        
    
    def list_repositories(self):
        url_list = []
        for repo in self.repos:
            url_list.append(repo['html_url'])
        return url_list

    def count_stars(self):
        star_count = 0
        for repo in self.repos:
            star_count += repo['stargazers_count']    
        return star_count

    def get(self, request, *args, **kwargs):
        context = {}
        context['url_list'] = self.url_list
        context['user_name'] = self.user_name
        context['star_count'] = self.star_count
        context['status_code'] = self.status_code
        context['message'] = self.message
        return JsonResponse(context)


def page_not_found(request, exception=None):
    #return HttpResponse("ni dziala")
    return HttpResponseRedirect(reverse('list_repos_of_a_user', kwargs={'user_name':'notfound'})) 