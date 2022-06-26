
from django.urls import path
from . import views

urlpatterns =[
    
    path('corny',views.corny, name='corny'),
    path('reddit_stories/<str:subreddit>',views.reddit, name='corny'),
    
    ]