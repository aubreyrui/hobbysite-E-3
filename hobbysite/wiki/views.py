from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import ArticleCategory, Article

class ArticleCategoryListView(ListView):
    model = ArticleCategory
    template_name = "wiki_article_list.html"

class ArticleDetailView( DetailView):
    model = Article
    template_name = "wiki_article_detail.html"

def article_list(request):
    categories = ArticleCategory.objects.all()
    ctx = {
    'categories': categories
    }
    return render(request, 'wiki_article_list.html', ctx)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = { 
        'article': article  
        }
    return render(request, 'wiki_article_detail.html', ctx)
# Create your views here.
