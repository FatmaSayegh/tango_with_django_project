from django.shortcuts import render
from django.http import HttpResponse 
from rango.models import Category

# each view returns an http response object
# after creating a view, map it using urls.py, where each url 

# Below are the views 

# request is an HttpRequest
def index(request):
    # load some stuff from the database
    
    # order in descending order, this the '-' begind likes
    # limit to 5, thus the [:5]
    category_list = Category.objects.order_by('-likes')[:5]
    
    # all replacements
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')