from django.contrib import admin
from .models import RetailData

# TO DO: Experimenting with Django's admin interface. Either remove or complete for prod
@admin.register(RetailData)
class RetailDataAdmin(admin.ModelAdmin):
    list_display = ['merchant', 'sku', 'country', 'retailer', 'segment']
    list_filter = ['segment', 'country']
    search_fields = ['merchant', 'sku', 'retailer']