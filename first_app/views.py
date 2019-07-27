from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def index(request):
    my_dict = {'insert_me': "Hello i am from views.py"}
    return render(request, 'first_app/index.html', context=my_dict)

def help(request):
    my_dict = {'insert_me': "hello, this is help page"}
    return render(request, 'first_app/help.html', context=my_dict)
