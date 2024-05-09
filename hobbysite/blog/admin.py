from django.contrib import admin
from .models import Article, ArticleCategory, Comment


class CommentAdmin(admin.ModelAdmin):
     model = Comment
    

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    

class ArticleInLine(admin.TabularInline):
    model = Article
     
     
class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)