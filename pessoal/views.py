# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpRequest
from datetime import  datetime
from .models import Article, Category
from django.views import generic

def indexView(request):

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pessoal/index.html',
        {
            'title': 'Home',
            'year': datetime.now().year,
        }
    )

def sobre(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pessoal/sobre.html',

        {
            'title': 'Sobre',
            'year': datetime.now().year,
        }
    )


def contato(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pessoal/contato.html',

        {
            'title': 'Contato',
            'year': datetime.now().year,
        }
    )

def noticias(request):
    assert isinstance(request, HttpRequest)
    category = str(request.GET['category'])
    posts = Article.objects.filter(category__name=category).order_by().reverse()
    title = {"lp":"Laboratório de Programação", "ie": "Instrumentação para o Ensino",
             "pds": "Precesso de Desenvolvimento de Software", "ieh": "Informática para o Ensino"}

    return render(
        request,
        'pessoal/posts.html',
        {
            'title': title[category],
            'year' : datetime.now().year,
            'posts' : posts
        }
    )

class NoticiaDetailView(generic.DetailView):
    model = Article
    template_name = 'pessoal/notice.html'
