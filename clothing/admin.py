from django.contrib import admin
from clothing.models import Cloth
# Register your models here.

class ClothAdmin( admin.ModelAdmin):
    list_display = ['name', 'price', 'material_type']
    search_fields = ['name',]


admin.site.register(Cloth, ClothAdmin)