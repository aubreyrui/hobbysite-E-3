from django import forms
from .models import Article, ArticleCategory, Comment

class ArticleCreateForms(forms.ModelForm):
    
    
    class Meta:
        model = Article
        exclude = ['article_author', 'created_on', 'updated_on']


class ArticleUpdateForms(forms.ModelForm):
    
    
    class Meta:
        model = Article
        exclude = ['article_author', 'created_on']


class CommentForms (forms.ModelForm):
    
    
    class Meta:
        model = Comment
        fields = ['entry']