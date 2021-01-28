from django.shortcuts import render
from django.http import HttpResponse 


# each view returns an http response object
# after creating a view, map it using urls.py, where each url 

# Below are the views 

# request is an HttpRequest
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")