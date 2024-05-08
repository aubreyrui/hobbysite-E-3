from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import ArticleDetailView, ArticleListView, ArticleCreateView, ArticleUpdateView

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='blog'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='blog_detail'),
    path('article/add', ArticleCreateView.as_view(), name='blog_write'),
    path('article/<int:pk>/edit', ArticleUpdateView.as_view(), name='blog_edit')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = 'blog'