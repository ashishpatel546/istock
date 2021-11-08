from django.db import models
from django.utils.html import format_html

# Create your models here.

class Service(models.Model):
    service_id = models.BigAutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    url = models.CharField(max_length=50)
    service_pic = models.ImageField(upload_to = 'services/')

    def __str__(self) -> str:
        return self.title
    
    def image_tag(self):
        return format_html(f'<img src="/media/{self.service_pic}" alt="myimg" style = "width:50px; border-radius:50%;"/>')
    def description(self):
        return self.desc[0:70]

class CustomerQuery(models.Model):
    query_id= models.BigAutoField(primary_key=True, auto_created=True)
    cust_name = models.CharField(max_length=100)
    cust_email = models.EmailField(max_length=254)
    cust_phone = models.CharField(max_length=15)
    query_product = models.CharField(max_length=100)
    query_message= models.TextField()
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.query_id}-->{self.cust_name}"