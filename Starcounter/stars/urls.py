from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<slug:user_name>/', views.list_repos_of_a_user, name = 'list_repos_of_a_user'),
]