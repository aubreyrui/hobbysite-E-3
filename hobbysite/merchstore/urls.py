from django.urls import path
from .views import ProductDetailView, ProductListView

urlpatterns = [
    path('items', ProductListView.as_view(), name="product_list"),
    path('item/<int:pk>', ProductDetailView.as_view(), name="product_detail"),
]

app_name = "merchstore"