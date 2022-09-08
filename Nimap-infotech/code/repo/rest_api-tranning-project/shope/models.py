from django.db import models

# Create your models here.
class Categorie(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.title

class ProductStatus(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = "product_status"

class ProductStatusChoice(models.IntegerChoices):
    active = 1
    inactive = 0

# product.status == ProductStatusChoice.active

class Product(models.Model):
    category_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True, related_name='product_categories')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    product_status = models.CharField(max_length=100, choices=ProductStatusChoice.choices, default=ProductStatusChoice.new)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self) -> str:
        return self.title

class Collection(models.Model):
    name=models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self) -> str:
        return self.name

class Collection_product(models.Model):
    collection_id = models.ForeignKey(Collection,on_delete=models.IntegerField,null=True)
    Product_id = models.ForeignKey(Product,on_delete=models.IntegerField,null=True)

