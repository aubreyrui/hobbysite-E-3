from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect


from .models import Article, ArticleCategory, Comment, Profile
from .forms import ArticleCreateForms, ArticleUpdateForms, CommentForms


class ArticleListView(ListView):
    model = Article
    template_name = 'blog_article_list.html'
    
class ArticleList(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "blog_article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_category"] = ArticleCategory.objects.all()
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog_article_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_category"] = ArticleCategory.objects.all()
        context["comments"] = Comment.objects.all()
        context["form"] = CommentForms()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForms(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.author = Profile.objects.get(user = self.request.user)
            comment.article = self.get_object()
            comment.entry = form.cleaned_data.get('entry')
            comment.save()
            return HttpResponseRedirect(request.path)
        else: 
            self.object_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            context["form"] = form 
            return self.render_to_response(context)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "blog_article_create.html"

    form_class = ArticleCreateForms

    def form_valid(self, form):
        form.instance.article_author = self.request.user.profile
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = "blog_article_update.html"

    form_class = ArticleUpdateForms

    def form_valid(self, form):
        article = self.get_object() 
        form.instance.article = article
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)