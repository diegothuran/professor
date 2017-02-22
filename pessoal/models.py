# Create your models here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from collections import defaultdict

import datetime


# Create your models here.

class Disciplinas(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.name

class ArticleManage(models.Manager):
    def archive(self):
        date_list = Article.objects.datetimes('created_time', 'month', order='DESC')
        date_dict = defaultdict(list)
        for d in date_list:
            date_dict[d.year].append(d.month)
        return sorted(date_dict.items(), reverse=True)


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
    )

    objects = ArticleManage()

    title = models.CharField(verbose_name='Título', max_length=70)
    body = models.TextField(verbose_name='Texto')
    created_time = models.DateTimeField(verbose_name='Data de Criação')
    last_modified_time = models.DateTimeField(verbose_name='Última modificação')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField(verbose_name='Resumo', max_length=54, blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    topped = models.BooleanField(default=False)

    category = models.ForeignKey('Category', verbose_name='Categoria', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-last_modified_time']

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'article_id': self.pk})


class Category(models.Model):
    name = models.CharField('Nome', max_length=20)
    created_time = models.DateTimeField('Criado em', auto_now_add=True)
    last_modified_time = models.DateTimeField('Última Modificação', auto_now=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('Nome', max_length=20)
    created_time = models.DateTimeField('Criado em', auto_now_add=True)
    last_modified_time = models.DateTimeField('Última Modificação', auto_now=True)

    def __str__(self):
        return self.name



class BlogComment(models.Model):
    user_name = models.CharField('Usuário', max_length=100)
    user_email = models.EmailField('Email', max_length=255)
    body = models.TextField('Texto')
    created_time = models.DateTimeField('Criado em', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='Artigo', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]
