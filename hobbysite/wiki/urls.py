from django.urls import path
from .views import ArticleCategoryListView, ArticleDetailView, ArticleCreateView

urlpatterns = [
    path('wiki/articles', ArticleCategoryListView.as_view(), name = 'wikipage'),
    path('wiki/article/<int:pk>', ArticleDetailView.as_view(), name = 'wiki_detail'),
    path('wiki/article/add', ArticleCreateView.as_view(), name= 'wiki_create')
]

app_name = 'wiki'