from django.shortcuts import render ,get_object_or_404 ,redirect   
from .models import News
from main.models import Main



def news_detial(request,word):
    
    
    #site = Main.objects.filter(pk=1) روش اول که for لازم دارد

    site = Main.objects.get(pk=1)
    news= News.objects.filter(name=word)
    return render(request ,'front/news_detial.html', {'site': site,'news':news,'word':word})


def news_list(request):

    news = News.objects.all()    

    return render(request , 'back/news_list.html',{'news':news})


def form(request):

    if request.method == "POST":
        
        writer = request.POST.get("writer")
        newstitle = request.POST.get("newstitle")
        newstxt = request.POST.get("newstxt")
        newsdate = request.POST.get("newsdate")
        newsimage = request.POST.get("newsimage")
        cat = request.POST.get("cat")

        if writer == "" or newstitle == "" or newstxt == "" or newsdate == "" or cat == "" :
            return render(request , 'back/error.html')
        
        b = News(name = newstitle , body = newstxt , date = newsdate , writer = writer ,  catagory = "-" , short_txt = "-" , image = newsimage , catid = "0" )
        b.save()
        return redirect(news_list)

    return render(request , 'back/forms.html')


def profile(request):

    
    return render(request , 'back/profile.html')
