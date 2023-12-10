from django.db import models
from category.models import CategoryModel
import os


# Create your models here.
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=500,null = True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True)
    # sale = models.IntegerField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_flag = models.BooleanField(default=False)
    image = models.ImageField(null=True,upload_to="images/")
    category = models.ForeignKey(CategoryModel,on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.product_name
    