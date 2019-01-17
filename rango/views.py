from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    # construct a dict to pass to the template engine as its context
    # note the key boldmessage is the same as {{boldmessage}} in the template
    context_dict={'boldmessage':"crunchy, creamy,cookie, candy, cup"}

    #return a rendered response to send to the client
    #we make use of the shortcut func to make our lives easier
    # note that  the first parameter is the template we wish to use

    return render(request,"rango/index.html",context=context_dict)
