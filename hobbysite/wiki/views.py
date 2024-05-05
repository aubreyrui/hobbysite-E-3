from django.shortcuts import render, redirect
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
    related_articles = Article.objects.filter(category = article.category).exclude(article) #all articles in category without the same article

    for related_article in related_articles: #to delete and to fix
        print(related_article.title)

    ctx = { 
        'article': article, 
        'related_articles': related_articles
        }
    return render(request, 'wiki_article_detail.html', ctx)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "wiki_article_create.html"
    form_class = ArticleCreateForms

    def form_valid(self, form):
        form.instance.article_author = self.request.user.profile #article assigned author is the user creating it
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "wiki_article_update.html"
    form_class = ArticleUpdateForms

    def form_valid(self, form):
        article = self.get_object()#gets the article then passes it to the instance 
        form.instance.article = article
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

    ### to add def form valid

def add_comment(request, pk): ### not sure yet
    article = Article.objects.get(pk=pk) #get article we want to comment on
    if request.method == 'POST':
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.article = article # whicher article it goes to/connected
            comment.author = request.user.profile
            comment.save()
        return redirect('article_detail', pk=pk)
    
    
# Create your views here.
    
