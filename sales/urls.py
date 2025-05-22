from django.urls import path
from . import views


urlpatterns = [path('',views.sales,name="sales")]