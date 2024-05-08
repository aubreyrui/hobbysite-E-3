from django.contrib import admin
from .models import Article, ArticleCategory, Comment


class CommentInLine(admin.TabularInline):
     model = Comment
    

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [CommentInLine]

    search_fields = [
        "title",
    ]

    list_display = ["title", "author", "category"]

    list_filter = [
        "created_on",
        "updated_on",
    ]

    fields = ["title", "author", "category", "entry", "header_image"]
    

class ArticleInLine(admin.TabularInline):
    model = Article
     
     
class ArticleCategoryAdmin(admin.ModelAdmin):
    model = ArticleCategory
    inlines = [ArticleInLine]
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Comment, CommentInLine)