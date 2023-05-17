from django.shortcuts import render
from django.http import HttpResponse

from .models import AccessRecord,Webpage,Topic

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}


    #my_dict = {'insert_content': "Hello I.m from firstapp"}
    return render(request, 'firstapp/index.html', context=date_dict)
