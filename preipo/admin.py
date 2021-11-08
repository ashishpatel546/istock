from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from preipo.models import PREIPO
# from django.utils.html import strip_tags


class PreipoAdmin(admin.ModelAdmin):
    list_display = ('image_tag','Script_Name', 'Buying_Price', 'Selling_Price')
    search_fields= ('Script_Name',)
    

# Register your models here.
admin.site.register(PREIPO, PreipoAdmin)