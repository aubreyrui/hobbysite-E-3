from django.contrib import admin
from .models import Article, ArticleCategory, Comment

class ArticleCategoryAdmin(admin.ModelAdmin):
     model = ArticleCategory

class ArticleAdmin(admin.ModelAdmin):
     model = Article

class CommentAdmin(admin.ModelAdmin):
     model = Comment
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
