from django.contrib import admin

from mutualFund.models import Service, CustomerQuery

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'description')
    search_fields=('title',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(CustomerQuery)