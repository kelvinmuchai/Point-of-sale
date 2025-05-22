from django.db import models
from PIL  import Image
# Create your models here.
from django.urls import reverse
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('dashboard')
    

    def __str__(self):
        # Show full path e.g., "Food & Beverages > Snacks"
        if self.parent:
            return f"{self.parent} > {self.name}"
        return self.name
    

class Products(models.Model):
    p_name = models.CharField(max_length=255,unique=True)
    p_description = models.TextField(max_length=200)
    p_price = models.DecimalField(max_digits=10,decimal_places=2)
    p_image = models.ImageField(default='default.jpg',upload_to='productsimg')
    p_costprice = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    p_stock = models.PositiveIntegerField(default=0)
    p_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        related_name='products'
    )



    def clean(self):
        if self.p_costprice >= self.p_price:
            raise ValidationError("Buying price must be lower than selling price")

    
    def __str__(self):
        return(self.p_name)
    #access the created product
    def get_absolute_url(self):
        return reverse('product-detail',kwargs={'pk':self.pk})
    
    def  save(self):
        super().save()
        

        img = Image.open(self.p_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.p_image.path)





        


