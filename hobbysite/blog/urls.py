from django.urls import path
from .views import ArticleDetailView, ArticleCategoryListView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('articles', ArticleCategoryListView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='blog_detail'),
    path('article/add', ArticleCreateView.as_view(), name= 'blog_write'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name = 'blog_edit')
]

app_name = 'blog'