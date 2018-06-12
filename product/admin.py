from django.contrib import admin

# Register your models here.

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id', 'product_sku', 'product_name', ]

#    def get_name(self, obj):
#        return obj.author.name
 #   get_name.admin_order_field  = 'product_sku'  #Allows column order sorting
 #   get_name.short_description = 'product_name'  #Renames column head

    #Filtering on side - for some reason, this works
    #list_filter = ['title', 'author__name']

admin.site.register(Product, ProductAdmin)