from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProductsListView.as_view(),name="home-page"),
    path('productssearch/',views.ProductsSearch,name='products-search'),
    path('newproduct/',views.ProductsCreateView.as_view(),name='create-product'),
    path('product/<int:pk>/update/',views.ProductsUpdateView.as_view(),name='product-update'),
    path('product/<int:pk>/delete/',views.ProductDeleteView.as_view(),name='product-delete'),
    path('dashboard/',views.CategoryListView.as_view(),name='dashboard'),
    path('product/<int:pk>/',views.product_detail,name='product-detail'),
    path('newcategory/',views.CategoryCreateView.as_view(),name='newcategory')

]

