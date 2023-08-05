from django.shortcuts import render
from django.http import HttpResponse
from .forms import stuform
import datetime

# Create your views here.
def home(request):
    return HttpResponse('<h1>This is student list</h1><br>we have 10 numbers')
def  datetime1(request):
    d=datetime.datetime.now()
    return HttpResponse(d)
def index(request):
    return render(request,'index.html')
def index2(request):
    a=[
        {'name':'faizan','age':24,'email':'f@gmail.com'},
        {'name':'faizan1','age':25,'email':'i@gmail.com'},
        {'name':'faizan2','age':26,'email':'j@gmail.com'},
        {'name':'faizan3','age':27,'email':'k@gmail.com'},
        {'name':'faizan4','age':28,'email':'l@gmail.com'},
    ]


    return render(request,'index2.html',{'a1':a})

def index3(request):
    a2=[
        {'name': 'tomato', 'record':8},
        {'name': 'onion', 'record':7},
        {'name': 'garlic', 'record':9},
        {'name': 'corn', 'record':0},
    ]


    return render(request,'index3.html',{'a1':a2})

def create(request):
    f=stuform()
    return render (request,'create.html',{'form':f})