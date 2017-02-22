from django.contrib import admin
from .models import Article, BlogComment, Category, Disciplinas


admin.site.register(Disciplinas)
admin.site.register(Article)
admin.site.register(BlogComment)
admin.site.register(Category)

