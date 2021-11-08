from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html

# Create your models here.
class PREIPO(models.Model):
    S_No = models.BigAutoField(primary_key=True, auto_created=True)
    Script_Name= models.CharField(max_length=100)
    Buying_Price = models.IntegerField()
    Selling_Price = models.IntegerField()
    # Desc = models.TextField()
    Desc = HTMLField()
    url = models.CharField(max_length=100)
    Script_pic = models.ImageField(upload_to = 'IPO/')

    def image_tag(self):
        return format_html(f'<img src="/media/{self.Script_pic}" alt="myimg" style = "width:50px; border-radius:50%;"/>')

    def __str__(self) -> str:
        return self.Script_Name