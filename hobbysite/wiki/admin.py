from django.contrib import admin
from .models import Article, ArticleCategory

class ArticleCategoryAdmin(admin.ModelAdmin):
     model = ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
     model = Article
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)

# Register your models here.
