# Import Product Model
from django.contrib import admin
from .models import Product, Offer

# Create an Offer class to allow offers in Admin area via a tuple


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')

# Create a ProductAdmin class to edit objects in the Admin area


class ProductAdmin(admin.ModelAdmin):
    # Set which columns which are to displayed via a tuple
    list_display = ('name', 'price', 'stock')

# Use admin object and site object, to pass Product class
# This lets us manage Product in the /admin area of our site.

# Register objects to Admin area


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)


