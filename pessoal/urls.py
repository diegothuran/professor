from django.conf.urls import url, include
from django.contrib import admin
import views

app_name = 'pessoal'

urlpatterns = [
    url(r'^$', view=views.indexView, name='home'),
    url(r'^sobre/$', view=views.sobre, name='sobre'),
    url(r'^contato/$', view=views.contato, name='contato'),
    url(r'^cadeira/$', view=views.noticias, name='noticia'),
    url(r'^post/(?P<pk>[0-9]+)/$', view=views.NoticiaDetailView.as_view(), name='post'),

]