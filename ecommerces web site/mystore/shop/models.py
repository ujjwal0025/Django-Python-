from django.db import models

# Create your models here.
class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    publice_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default = "")
    

class contact(models.Model):
    contact_id = models.AutoField
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.IntegerField(default="")
    desc = models.CharField(max_length=500,default="")
    


    def __str__(self):
        return self.name


class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    addresh = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    zip_code = models.CharField(max_length=90)
    phone = models.IntegerField(max_length=12)

class orderupdate(models.Model):
    update_id = models.AutoField(primary_key = True)
    order_id  = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

def __str__(self):
    return self.update_desc[0:7]+"....."
