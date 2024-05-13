from django.db import models
from django.urls import reverse
from user_management.models import Profile


class ArticleCategory(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(null = True, blank = True)


    class Meta:
        ordering = ['name']     # name in ascending order
        verbose_name = 'article category'
        verbose_name_plural = 'article categories'
        
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    article_author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='blog_article_author')
    category = models.ForeignKey(ArticleCategory, null=True, on_delete=models.SET_NULL, related_name='blog_articles')
    entry = models.TextField()
    header_image = models.ImageField(upload_to='images/', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_on']   # due date in descending order
        

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=[self.pk])
    

class Comment(models.Model):
    comment_author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL, related_name='blog_comment_author')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='blog_comment_article')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)    
    
    
    class Meta:
        ordering = ['-created_on']  # for the comments to be arranged from latest to oldest
        
    def __str__(self):
        return f"Comment by {self.comment_author} on {self.article.user}"