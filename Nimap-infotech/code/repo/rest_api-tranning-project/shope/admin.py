from django.contrib import admin
from shope.models import Categorie,Product,Collection,Collection_product, ProductStatus
# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'created_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','category_id','title','price', 'created_at')

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at')


@admin.register(Collection_product)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id','collection_id','Product_id')

admin.site.register(ProductStatus)