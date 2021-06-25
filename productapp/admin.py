from django.contrib import admin
from productapp.models import Category,Size,ProType,Product

# Register your models here.

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(ProType)
admin.site.register(Product)
