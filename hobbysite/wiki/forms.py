from django import forms
from .models import Article, Comment, ArticleCategory

class ArticleCreateForms(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
        category = forms.ModelChoiceField(queryset= ArticleCategory.objects.all()) #

class ArticleUpdateForms(forms.ModelForm): #basically a template!
    class Meta:
        model = Article
        exclude = ["created_on", "Author"]

class CommentForms (forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'