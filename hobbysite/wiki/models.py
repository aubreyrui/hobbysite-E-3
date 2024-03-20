from django.db import models
from django.urls import reverse

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
    category = models.ForeignKey(ArticleCategory, on_delete = models.CASCADE, related_name = 'article')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True) #https://www.scaler.com/topics/django/django-datetimefield/ \
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('wiki:wiki_detail', args=[self.pk])
    
    class Meta:
        ordering = ['-created_on'] #https://docs.djangoproject.com/en/5.0/ref/models/options/
# Create your models here.
