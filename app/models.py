from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
  ("Pending","Pending"),
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel')
)

STATE_CHOICES = (
  ('Andaman & Nicobar Islands','Andaman & Nicobar Islands'),
  ('Andhra Pradesh','Andhra Pradesh'),
  ('Arunachal Pradesh','Arunachal Pradesh'),
  ('Assam','Assam'),
  ('Bihar','Bihar'),
  ('Chandigarh','Chandigarh'),
  ('Chhattisgarh','Chhattisgarh'),
  ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
  ('Daman and Diu','Daman and Diu'),
  ('Delhi','Delhi'),
  ('Goa','Goa'),
  ('Gujarat','Gujarat'),
  ('Haryana','Haryana'),
  ('Himachal Pradesh','Himachal Pradesh'),
  ('Jammu & Kashmir','Jammu & Kashmir'),
  ('Jharkhand','Jharkhand'),
  ('Karnataka','Karnataka'),
  ('Kerala','Kerala'),
  ('Lakshadweep','Lakshadweep'),
  ('Madhya Pradesh','Madhya Pradesh'),
  ('Maharashtra','Maharashtra'),
  ('Manipur','Manipur'),
  ('Meghalaya','Meghalaya'),
  ('Mizoram','Mizoram'),
  ('Nagaland','Nagaland'),
  ('Odisha','Odisha'),
  ('Puducherry','Puducherry'),
  ('Punjab','Punjab'),
  ('Rajasthan','Rajasthan'),
  ('Sikkim','Sikkim'),
  ('Tamil Nadu','Tamil Nadu'),
  ('Telangana','Telangana'),
  ('Tripura','Tripura'),
  ('Uttarakhand','Uttarakhand'),
  ('Uttar Pradesh','Uttar Pradesh'),
  ('West Bengal','West Bengal'),
)

CATEGORY_CHOICES = (
 ('M', 'Mobile'),
 ('L', 'Laptop'),
 ('TW', 'Top Wear'),
 ('BW', 'Bottom Wear'),
)

class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.PositiveIntegerField()
    discounted_price=models.PositiveIntegerField()
    description=models.CharField(max_length=200, blank=True)
    brand=models.CharField(max_length=200, blank=True)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=200)
    product_image=models.ImageField( upload_to="product_image" )

    def __str__(self):
        return self.title

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField( max_length=200)
    locality=models.CharField( max_length=1000)
    city=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=6)
    state=models.CharField(choices=STATE_CHOICES, max_length=50)
    phone_number=models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    product=models.ForeignKey( Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity* self.product.discounted_price


class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    status=models.CharField(choices=STATUS_CHOICES,default="Pending" ,max_length=50)
    ordered_date=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.quantity* self.product.discounted_price



