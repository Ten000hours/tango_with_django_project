from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category,Page
def index(request):
    # construct a dict to pass to the template engine as its context
    # note the key boldmessage is the same as {{boldmessage}} in the template
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    #return a rendered response to send to the client
    #we make use of the shortcut func to make our lives easier
    # note that  the first parameter is the template we wish to use

    return render(request,"rango/index.html",context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)
        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
            context_dict['category'] = None
            context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)
def about(request, category_name_slug):
    context_dict={}
    return render(request, 'rango/category.html', context_dict)