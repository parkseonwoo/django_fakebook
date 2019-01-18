
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse 
from django.shortcuts import render, redirect

from fakebook.models import Article



def add_func(request, num1, num2): 
    result = num1 + num2
    content ="sfdgerg{}{}{}".format(num1, num2, result) 
    return HttpResponse(content)  
    
def home_func(request): 
    return render(request, 'index.html') 

def newsfeed_func(request):
    articles = Article.objects.all().order_by('-created_at') 
    return render(request, 'newsfeed.html',{'articles':articles})

def new_feed_func(request):
    if request.method == 'POST': #게시글 올리기로 들어온것
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['content'] != '' and request.POST['password'] != '':
            plus_text = request.POST['content']

            new_article = Article.objects.create(
                author = request.POST['author'],
                title = request.POST['title'],
                text = plus_text,
                password = request.POST['password'])
        return redirect(f'/newsfeed/')
    
    return render(request,'new_feed.html')

#http://127.0.0.1:5010/add/10/20
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/<int:num1>/<int:num2>/',add_func), 
    path('home/',home_func), 
    path('newsfeed/',newsfeed_func),
    path('new/',new_feed_func),
]
