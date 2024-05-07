from django.contrib import admin
from .models import Article, ArticleCategory, Comment


class ArticleAdmin(admin.ModelAdmin):
    model = Article
     
     
class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    

class CommentAdmin(admin.ModelAdmin):
     model = Comment
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentAdmin)