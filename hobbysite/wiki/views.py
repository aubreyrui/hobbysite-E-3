from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.db.models import Q

from .models import ArticleCategory, Article
from .forms import ArticleCreateForms, CommentForms, ArticleUpdateForms

class ArticleCategoryListView(ListView):
    model = ArticleCategory
    template_name = "wiki_article_list.html"

class ArticleDetailView( DetailView):
    model = Article
    template_name = "wiki_article_detail.html"

def article_list(request):
    my_articles = Article.objects.filter(article_author = request.user) #https://stackoverflow.com/questions/44464544/django-authentication-filter-only-user-created-not-all-records-in-view
    other_articles = Article.objects.filter(~Q(article_author = request.user)) #https://docs.djangoproject.com/en/5.0/topics/db/queries/
    categories = ArticleCategory.objects.all()
    ctx = {
    'my_articles': my_articles,
    'categories': categories,
    'other_articles': other_articles
    }
    return render(request, 'wiki_article_list.html', ctx)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    ctx = { 
        'article': article  
        }
    return render(request, 'wiki_article_detail.html', ctx)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "wiki_article_create.html"
    form_class = ArticleCreateForms

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "wiki_article_update.html"
    form_class = ArticlUpdateForms
# Create your views here.
    
