from django.urls import path, include
from . import views






urlpatterns = [
    path('news/<word>/',views.news_detial,name='news_detial'),
    path('panel/news/list/',views.news_list,name='news_list'),

]
