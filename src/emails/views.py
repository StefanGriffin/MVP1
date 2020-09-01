from django.shortcuts import render
from django.http import HttpResponse, Http404 
from .models import EmailEntry

html_str = "<!doctype html><html><body><h1>{email}</body></html>"

def email_entry_get_view(request, id=None, *args, **kwargs ):
    # print(args, kwargs)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    # return HttpResponse(f"<h1>Hello Stef Griffin</h1>")
    return render(request, "get.html", {"object": obj})



    
