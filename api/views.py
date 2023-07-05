from django.http import JsonResponse
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from product.models import Category, Product, Basket
from .serializers import ProductSerializer, BasketSerializer, BasketItemsSerializer


# Create your views here.
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs['pk'])


# class AddBasketProductView(generics.CreateAPIView, generics.RetrieveAPIView):
#     serializer_class = BasketItemsSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         product = Product.objects.get(pk=self.kwargs['pk'])
#         return Basket.objects.filter(user=self.request.user, product=product)
#
#     def perform_create(self, serializer):
#         if self.get_queryset().exists():
#             raise ValidationError('This\'s product already been in basket!')
#         product = Product.objects.get(pk=self.kwargs['pk'])
#         serializer.save(user=self.request.user, product=product)

@api_view(['POST'])
def add_basket(request, pk):
    user = request.user
    product = Product.objects.get(pk=pk)
    baskets = Basket.objects.filter(user=user, product=product)
    if not baskets.exists():
        basket = Basket.objects.create(user=request.user, product=product)
        serializer = BasketItemsSerializer(basket, many=False)
        return Response(serializer.data, status=201)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        serializer = BasketItemsSerializer(basket, many=False)
        return Response(serializer.data, status=200)


class BasketListView(generics.ListAPIView):
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user)


class BasketItemsUpdateDeleteView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = BasketItemsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Basket.objects.filter(user=self.request.user, pk=self.kwargs['pk'])

    def perform_update(self, serializer):
        if int(self.request.data['quantity']) > 0:
            serializer.instance.quantity = int(self.request.data['quantity'])
            serializer.save()
