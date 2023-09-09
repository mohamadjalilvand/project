from django.shortcuts import render ,get_object_or_404 ,redirect   
from .models import News
from main.models import Main



def news_detial(request,word):
    
    
    #site = Main.objects.filter(pk=1) روش اول که for لازم دارد

    site = Main.objects.get(pk=1)
    news= News.objects.filter(name=word)
    return render(request ,'front/news_detial.html', {'site': site,'news':news,'word':word})

