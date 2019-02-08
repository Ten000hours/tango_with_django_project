from django.shortcuts import render
from django.http import HttpResponse
from rango.forms import PageForm
from rango.models import Category,Page
from rango.forms import CategoryForm
def index(request):
    # construct a dict to pass to the template engine as its context
    # note the key boldmessage is the same as {{boldmessage}} in the template
    category_list = Category.objects.order_by('-likes')[:5]
    # context_dict = {'categories': category_list}

    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'pages': page_list}
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
def about(request):
    # prints out whether the method is a GET or a POST
    print(request.method)
    # prints out the user name, if no one is logged in it prints `AnonymousUser`
    print(request.user)
    return render(request, 'rango/about.html', {})

def add_category(request):
    form= CategoryForm()

    ## A HTTP POST
    if request.method=="POST":
        form=CategoryForm(request.POST)

        #have we been provided with a valid form?
        if form.is_valid():
            # save the new category to the database
            form.save(commit=True)
            #now that the category is saved
            #we could give a confirmation
            #but since the most recent category added is on the index page
            # we can direct the user back to the index page
            return index(request)
        else:
            # the supplied form contained errors
            print(form.errors)

    return render(request,"rango/add_category.html",{"form":form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)