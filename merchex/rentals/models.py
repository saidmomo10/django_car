from django.db import models
from cars.models import Car
from customers.models import Customer


class Rental(models.Model):
    car = models.ForeignKey(Car, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField(null=True, blank=True)
    expected_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)

    STATUS_ON_TIME = 'Délai respecté'
    STATUS_DELAYED = 'Délai non respecté'

    @property
    def status(self):
        if self.return_date is not None and self.expected_date is not None:
            if self.return_date < self.expected_date:
                return self.STATUS_ON_TIME
            elif self.return_date == self.expected_date:
                return self.STATUS_ON_TIME
            else:
                return self.STATUS_DELAYED
        else:
            return 'En cours de location'

    
    
