from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField

# Create your models here.


class Insurance(models.Model):
    ins_id = models.BigAutoField(auto_created=True, primary_key=True)
    ins_name = models.CharField(max_length=100)
    ins_img = models.ImageField(upload_to = 'Insurance/')
    desc = HTMLField()
    url = models.CharField(max_length=100)

    def image_tag(self):
        return format_html(f'<img src="/media/{self.ins_img}" alt="myimg" style = "width:50px; border-radius:50%;"/>')

    def __str__(self) -> str:
        return self.ins_name