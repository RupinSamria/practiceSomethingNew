from django.http import HttpResponse
from django.shortcuts import render
# from ./models import tweet_id

# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Something</h1>")

def home_detail_view(request,tweet_id, *args, **kwargs):
    return HttpResponse(f"<h1>Something Id- {tweet_id}</h1>")