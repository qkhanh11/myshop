from django.contrib import admin
from django import forms
from .models import ProductModel

class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name", "price", "quantity", "create_at"]
    list_filter = ["create_at","category"]
    search_fields = ["product_name"]
    form = ProductAdminForm 
    

admin.site.register(ProductModel,ProductAdmin)
