from django.contrib import admin
from . import models

# Register your models here.
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('parent',)
    search_fields = ('name',)

admin.site.register(models.Products)
