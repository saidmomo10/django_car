from django.db import models
from rental.models import Rental

class Rental(models.Model):
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    status = 
    

    def __str__(self):
        return self.name
