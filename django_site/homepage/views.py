from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def home(request):
    name = "Suresh"
    html = "<html><body>Hi %s. dude whatssup seems to have worked!</body></html>" % name
    return HttpResponse(html)

def home_template(request):
    name = "Suresh"
    t = get_template('home.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)
