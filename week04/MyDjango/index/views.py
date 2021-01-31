from django.shortcuts import render
from django.shortcuts import redirect
from .models import DoubanFilms

# Create your views here.
from django.http import HttpResponse

###  从models取数据传给template  ###
from .models import Name

def index(request):
    return HttpResponse("Hello Django!")

def myyear(request, year):
    return render(request, 'yearview.html')

def year(request, year):
    return HttpResponse(year)
    # return redirect('/2020.html')

def name(request, **kwargs):
    return HttpResponse(kwargs['name'])

def films(request):
    films = DoubanFilms.objects.all()
    return render(request, 'doubanfilms.html', locals())