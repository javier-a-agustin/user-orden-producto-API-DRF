from django.contrib import admin

from api.models import Order, OrderDescription, Product

admin.site.register(Order)
admin.site.register(OrderDescription)
admin.site.register(Product)
