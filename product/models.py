from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=75, verbose_name='Title')
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=75, verbose_name='Title')
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE, verbose_name='Brand')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Category', default=1)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Price')
    image = models.ImageField(upload_to='product_image/', verbose_name='Product image')

    def __str__(self):
        return f'{self.title}-{self.price}$'


class Basket(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Product')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='User')
    quantity = models.PositiveSmallIntegerField(verbose_name='Quantity', default=1)

    def __str__(self):
        return f'{self.user.username}-{self.product.title}'
