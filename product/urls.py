from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.products,name='list'),
    path('detail/<int:id>', views.detail, name='detail'),
]