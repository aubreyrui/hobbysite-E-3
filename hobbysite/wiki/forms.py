from django import forms
from .models import Article, Comment, ArticleCategory

class ArticleCreateForms(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ["created_on", "wiki_article_author", "updated_on"]
        category = forms.ModelChoiceField(queryset= ArticleCategory.objects.all()) #https://forum.djangoproject.com/t/working-with-django-forms-hand-over-drop-down-list/21236

class ArticleUpdateForms(forms.ModelForm): #basically a template!
    class Meta:
        model = Article
        exclude = ["created_on", "wiki_article_author"]

class CommentForms (forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']