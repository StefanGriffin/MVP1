from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def email_entry_get_vieiw(request, *args, **kwargs ):
    obj = EmailEntry.objects.get(id=1)
    return HttpResponse(f"<h1>Hello {obj.email}</h1>")

    
