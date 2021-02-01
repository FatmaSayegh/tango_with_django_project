from django.shortcuts import render
from django.http import HttpResponse 
from rango.models import Category, Page
from rango.forms import CategoryForm
from django.shortcuts import redirect

# each view returns an http response object
# after creating a view, map it using urls.py, where each url 

# Below are the views 

# request is an HttpRequest
def index(request):
    # load some stuff from the database
    
    # order in descending order, this the '-' begind likes
    # limit to 5, thus the [:5]
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    # all replacements
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages_list
    
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        # get associated category
        category = Category.objects.get(slug=category_name_slug)
        
        # find associated pages
        pages = Page.objects.filter(category=category)
        
        # add to context
        context_dict['pages'] = pages
        context_dict['category'] = category
    
    except Category.DoesNotExist:
        # nothing
        context_dict['category'] = None
        context_dict['pages'] = None
        
    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)


def add_category(request):
    form = CategoryForm()
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)
    # Have we been provided with a valid form?
    if form.is_valid():
        # Save the new category to the database.
        form.save(commit=True)
        # Now that the category is saved, we could confirm this.
        # For now, just redirect the user back to the index view.
        return redirect('/rango/')
    else:
    # The supplied form contained errors -
        print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})   
    