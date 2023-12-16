from django.db import models
# Create your models here.
from django.contrib.auth.models import User



CATEGROY_CHOICES =(
    ('M','Mobile'),
    ('L','Leptop'),
    ('TW','Top Wear'),
    ('BW','Bottam Wear'),
    ('SW','Smart Watch'),
    ('SH','Shoes'),
    ('HD', 'Head Phone'),
    ('KP','Kurta Pajama'),
    ('FB','Foot Ball'),
    ('BG','Bag'),




)
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description=models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(choices = CATEGROY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='producting')

class Cart(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE) 
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)   
    






