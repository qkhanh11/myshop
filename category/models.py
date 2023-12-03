from django.db import models


# Create your models here.
class CategoryModel(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    delete_flag = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name