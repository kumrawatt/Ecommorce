from django.db import models
# Create your models here.
from django.contrib.auth.models import User

STATE_CHOICES = (
('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
('Andra Pradesh', 'Andra Pradesh'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Assam', 'Assam'),
('Bihar', 'Bihar'),
('Chhattisgarh', 'Chhattisgarh'),
('chandigarh', 'chandigarh'),
('dadra & Nagar Haveli', 'dadra & Nagar Haveli'),
('Delhi', 'Delhi'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Utter Pradesh', 'Utter Pradesh'),
('Andra Pradesh', 'Andra Pradesh'),
('Mumbai', 'Mumbai'),
('Mizoram', 'Mizoram'),
('Nagaland', 'Nagaland'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality=models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)
    
    def __str__(self):
        return str(self.id)






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

STATUS_CHOICES =(
    ('Accepted', 'Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel','Cancel'),
)  

class Orderplace(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1) 
    order_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default="panding")   






