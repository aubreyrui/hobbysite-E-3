from datetime import datetime
from django.db import models
from django.urls import reverse


class Commission(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField(null = False)
    people_required = models.IntegerField(null = False)
    created_on = models.DateField(null = False, auto_now_add = True)
    updated_on = models.DateField(null = False, auto_now = True)


    class Meta:
        ordering = ['created_on']
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("commissions:commissions_detail", args=str(self.pk))


class Comment(models.Model):
    entry = models.TextField(null = False)
    created_on = models.DateField(null = False, auto_now_add = True)
    updated_on = models.DateField(null = False, auto_now = True)
    comments = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='commissions')


    class Meta:
        ordering = ['-created_on']

        
    def __str__(self):
        return self.entry