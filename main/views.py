from django.shortcuts import render ,get_object_or_404 ,redirect   
from .models import Main


# Create your views here.

def home(request):
    
    
    #site = Main.objects.filter(pk=1) روش اول که for لازم دارد

    site = Main.objects.get(pk=1)
    return render(request ,'front/home.html', {'site': site})


def about(request):
    
    site = Main.objects.get(pk=1)
    return render(request ,'front/about.html', {'sitename': site})


