from django.db import models

# Create your models here.
class Order(models.Model):
    order_name=models.CharField(max_length=322)
    order_id=models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    order_status=models.CharField(max_length=32)
    number_of_orders=models.IntegerField
    stock_amount=models.IntegerField
    def __str__(self):
        return self.order_status
    



