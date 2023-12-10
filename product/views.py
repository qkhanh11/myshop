from django.shortcuts import render
from .models import ProductModel
from category.models import CategoryModel
from django.conf import settings
from django.db.models import Q
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def products(request):
    limit = settings.DEFAULT_LIMIT #3
    keyword = request.GET.get("keyword","")
    category1 = request.GET.get("category","")
    page = request.GET.get("page",1)
    sort = request.GET.get("sort")
    if keyword != ""and category1 !="":
        category2 = CategoryModel.objects.get(id=category1)
        product_list=ProductModel.objects.filter(
            Q(product_name__icontains=keyword)
            | Q(summary__icontains=keyword)
            | Q(description__icontains=keyword), category=category2
        )
    elif keyword == "" and category1 !="":
        category2 = CategoryModel.objects.get(id=category1)
        product_list=ProductModel.objects.filter( category=category2 )
    elif keyword != "" and category1 =="":
        product_list=ProductModel.objects.filter(
            Q(product_name__icontains=keyword)
            | Q(summary__icontains=keyword)
            | Q(description__icontains=keyword)
        )
        
    else:
        product_list = ProductModel.objects.all()
    if sort not in ["-create_at","create_at","product_name","price",'-price']:
        sort = settings.DEFAULT_SORT
    category = CategoryModel.objects.all()
    
    product_list = product_list.order_by(sort)
    product_list_paging = Paginator(product_list, limit)
    try:
        product_list_paging = product_list_paging.get_page(page)
    except PageNotAnInteger:
        product_list_paging = product_list_paging.get_page(1)
    except EmptyPage:
        product_list_paging = product_list_paging.get_page(product_list_paging.num_pages)
    context = {
        'products_list': product_list_paging,
        'category': category
    }
    return render(request,"product/list.html",context)


def detail(request,id):
    product = ProductModel.objects.get(id=id)
    context={
        "product": product,
    }
    return render(request,"product/detail.html",context)