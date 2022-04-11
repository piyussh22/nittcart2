from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Addpost1(models.Model):
    username= models.CharField( max_length=50)
    caption=models.CharField( max_length=60)
    pic=models.ImageField(upload_to='post')
    attachement=models.FileField(upload_to='post')
    

    def __str__(self):
        return self.username

class Registerform(models.Model):
    username=models.CharField( max_length=50)
    name=models.CharField( max_length=50)
    password=models.CharField( max_length=25)
    phone=models.CharField( max_length=60)
    
   

    
   

    def __str__(self):
        return self.username

