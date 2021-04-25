from django.urls import path
from . import views

urlpatterns = [
    path('<slug:user_name>/', views.Git_handler.as_view(), name = 'list_repos_with_stars'),
    
]