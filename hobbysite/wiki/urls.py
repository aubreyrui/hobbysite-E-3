from django.urls import path
from .views import ArticleCategoryListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('wiki/articles', ArticleCategoryListView.as_view(), name = 'wikipage'),
    path('wiki/article/<int:pk>', ArticleDetailView.as_view(), name = 'wiki_detail'),
    path('wiki/article/add', ArticleCreateView.as_view(), name= 'wiki_create'),
    path('wiki/article/1/edit', ArticleUpdateView.as_view(), name = 'wiki_update')
]

app_name = 'wiki'