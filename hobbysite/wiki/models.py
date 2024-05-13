from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = 'article category'
        verbose_name_plural = 'article categories'   

class Article(models.Model):
    title = models.CharField(max_length = 255)
    article_author = models.ForeignKey(Profile, null = True, on_delete= models.SET_NULL, related_name = "wiki_article_author" )
    category = models.ForeignKey(ArticleCategory, null = True, on_delete = models.SET_NULL, related_name = 'wiki_article')
    entry = models.TextField()
    header_image = models.ImageField(upload_to='images/', null = True) #toedit
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True) #https://www.scaler.com/topics/django/django-datetimefield/ \
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('wiki:wiki_detail', args=[self.pk])
    
    class Meta:
        ordering = ['-created_on'] #https://docs.djangoproject.com/en/5.0/ref/models/options/

class Comment(models.Model):
    comment_author = models.ForeignKey(Profile, null = True,on_delete= models.SET_NULL, related_name = "wiki_comment_author" )
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True) #https://www.scaler.com/topics/django/django-datetimefield/ \        
    
    def __str__(self):
        return self.entry
    
    class Meta:
        ordering = ['-created_on']
  


# Create your models here.
