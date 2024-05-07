from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.db.models import Q

from .models import ArticleCategory, Article, Comment
from .forms import ArticleCreateForms, CommentForms, ArticleUpdateForms

class ArticleCategoryListView(ListView):
    model = ArticleCategory
    template_name = "wiki_article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "wiki_article_detail.html"

    def get_context_data(self, **kwargs): # from Django Book
        context = super().get_context_data(**kwargs) #overides the other get_context
        context['form'] = CommentForms() #instances of form is the comment forms
        context['comments'] = Comment.objects.all() #connects each comment to all the 
        context['articles'] = Article.objects.all()
        context['header_image'] = Article.header_image
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.comment_author = self.request.user.profile
            comment.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object_list = self.get_queryset()
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)
    
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
    
# Create your views here.
    
