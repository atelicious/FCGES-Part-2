from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    valuation = models.DecimalField(default=0, max_digits=17, decimal_places=4)

    def __str__(self):
        return f'{self.name}'

    def update_valuation(self, value):
        self.valuation = self.valuation + value

class Stock(models.Model):
    stock_id = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.DecimalField(max_digits=17,decimal_places=4, null=True)

    def __str__(self):
        return f'{self.stock_id} - {self.name}'

class PurchaseOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True)
    stock_qty = models.IntegerField(default=0, null=True, blank=True)
    price = models.DecimalField(max_digits=17, decimal_places=4, null=True)

    def __str__(self):
        return f'{self.stock} - {self.stock_qty} - {self.price}'
