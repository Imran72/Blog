from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


def index(request):
    listArticles = Article.objects.order_by('-pubDate')[:5]
    return render(request, 'articles/list.html', {"listArticles": listArticles})


def detail(request, articleID):
    try:
        a = Article.objects.get(id=articleID)
    except:
        raise Http404("Статья не найдена!")
    comments = a.comment_set.order_by('-id')[:10]
    return render(request, "articles/detail.html", {'article': a, "comments": comments})


def leave_comment(request, articleID):
    try:
        a = Article.objects.get(id=articleID)
    except:
        raise Http404("Статья не найдена!")

    a.comment_set.create(authorName=request.POST["name"], commentText=request.POST["text"])
    return HttpResponseRedirect(reverse("articles:detail", args=(a.id,)))
