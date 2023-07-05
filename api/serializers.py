from rest_framework import serializers

from product.models import Category, Product, Basket


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.ReadOnlyField(source='brand.title')
    category = serializers.ReadOnlyField(source='category.title')

    class Meta:
        model = Product
        fields = '__all__'


class BasketSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.pk')
    sum = serializers.SerializerMethodField(method_name='sum_quantity')
    product = ProductSerializer()

    class Meta:
        model = Basket
        fields = '__all__'

    def sum_quantity(self, obj):
        return obj.quantity * obj.product.price


class BasketItemsSerializer(serializers.ModelSerializer):
    # quantity = serializers.IntegerField(default=1)

    class Meta:
        model = Basket
        fields = ['pk']
