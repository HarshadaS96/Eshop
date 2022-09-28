from django.db import models
from .category import Category


# Create your models here.


# class Category(models.Model):
#  name = models.CharField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default=0)
    image = models.ImageField(upload_to='products/')
    rating = models.IntegerField(default=0)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.IntegerField(default=0, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=200, null=True)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE())
