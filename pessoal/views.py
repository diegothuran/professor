from django.shortcuts import render
from django.http import HttpRequest
from datetime import  datetime
# Create your views here.

def indexView(request):

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'pessoal/index.html',
        {
            'title': 'Home Page',
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