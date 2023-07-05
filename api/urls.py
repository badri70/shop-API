from django.urls import path

from .views import *


urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('products/<int:pk>/add_basket/', add_basket),
    #path('products/<int:pk>/add_basket/', AddBasketProductView.as_view()),
    path('basket/', BasketListView.as_view()),
    path('basket/<int:pk>/', BasketItemsUpdateDeleteView.as_view()),
]
