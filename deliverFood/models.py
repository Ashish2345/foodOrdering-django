from audioop import reverse
import imp
from operator import mod
from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from django.urls import reverse
# Create your models here.
class Catg_Foods(models.Model):
    
    catg_name = models.CharField(max_length=100)
    catg_desc = models.TextField()
    slug = models.SlugField(max_length=100,unique=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
  


    def __str__(self) :
        return self.catg_name

class Food_Items(models.Model):
    category = models.ForeignKey(Catg_Foods,on_delete=models.CASCADE)
    food_name = models.CharField(max_length=100,unique=True)
    food_desc = models.TextField()
    food_price = models.DecimalField(max_digits=5, decimal_places=2)
    food_pic = models.ImageField(upload_to="the_uploaded_images")
    slug = models.SlugField(unique=True,max_length=100)
    modified_date = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)
    rating = models.IntegerField(default=0,validators= [ MaxValueValidator(5),MinValueValidator(0) ],null=True)
    

    def get_url(self):
        return reverse("food_detail",args=[self.category.slug, self.slug])

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

  


    def __str__(self):
        return self.food_name