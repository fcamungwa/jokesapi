from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests as r
# Create your views here.

@api_view(['GET'])
def corny(requests):

    return Response('hello')


@api_view(['POST'])
def reddit(requests, subreddit):

    if len(str(subreddit))==0:
        link = r"https://www.reddit.com/r/BestofRedditorUpdates/top.json?limit=200&t=year"
    else :
        link =f"https://www.reddit.com/r/{subreddit}/top.json?limit=200&t=year"

    data = r.get(link,headers={"Content-Type":"text",'User-agent': 'your bot 0.1'})
    stream = data.json()['data']['children']
    storylist = []
    for x in stream:
        story_text = x['data']['selftext']
        story_title = x['data']['title']
        storylist.append((story_title,story_text))

    return Response({'storylines': storylist})
    