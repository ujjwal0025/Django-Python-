from django.db import models

# Create your models here.
class blogger(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    heading1 = models.CharField(max_length=500)
    cont_heading1 = models.CharField(max_length=500)
    heading2 = models.CharField(max_length=500)
    cont_heading2 = models.CharField(max_length=500)
    thumnail = models.ImageField(upload_to="shop/images",default = "")


    def __str__(self):
        return self.title
