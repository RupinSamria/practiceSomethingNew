from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet


# Create your views here.

def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Something</h1>")
    return render(request, "pages/home.html", context={}, status=200)



def tweet_list_view(request, *args, **kwargs):
    """
    Endpoints
    REST API VIEW
    Consume by Javascript or Swift or Java/iOS/Android
    return json data
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_detail_view(request,tweet_id, *args, **kwargs):
    """
    Endpoints
    REST API VIEW
    Consume by Javascript or Swift or Java/iOS/Android
    return json data
    """
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data, status=status)

    
    
    
    
    
    
        
    # try:
    #     obj = Tweet.objects.get(id=tweet_id)
    # except:
    #     raise Http404
    # return HttpResponse(f"<h1>Something Id- {tweet_id}, Content-{obj.content}</h1>")