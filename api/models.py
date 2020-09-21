from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return self.name.capitalize()

class Order(models.Model):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    finalPrice = models.FloatField(default=0, blank=False)
    
    def save(self, *args, **kwargs):
        
        final_price = 0

        try:
            datos = OrderDescription.objects.filter(order=self)
        except:
           final_price = 0
           datos = []
        print("datos", datos)

        for e in datos:
            final_price += e.product.price * e.quantity
            print(final_price)

        self.finalPrice = final_price
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return "Order by: {}, order id: {}".format(self.createdBy.username, self.pk)

class OrderDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        super(OrderDescription, self).save(*args, **kwargs)
        Order.save(self.order)

    def __str__(self):
        return 'Product name: {}, quantity: {}, id: {}'.format(self.product.name, self.quantity, self.pk)
    