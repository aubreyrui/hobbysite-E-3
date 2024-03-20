from django.urls import path
from .views import ArticleCategoryListView, ArticleDetailView

urlpatterns = [
    path('wiki/articles', ArticleCategoryListView.as_view(), name = 'wikipage'),
    path('wiki/article/<int:pk>', ArticleDetailView.as_view(), name = 'wiki_detail'),
]

app_name = 'wiki'