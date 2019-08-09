from django.shortcuts import render
from django.http.response import HttpResponse

from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

def index(request):
    webpages = AccessRecord.objects.order_by('date')

    # access_records is mentioned in html file
    date_dict = {'access_records': webpages}
    return render(request, 'first_app/index.html', context=date_dict)

def help(request):
    my_dict = {'insert_me': "hello, this is help page"}
    return render(request, 'first_app/help.html', context=my_dict)
