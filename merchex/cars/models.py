from django.db import models
from categories.models import Category

class Car(models.Model):
    name = models.CharField(null=True, max_length=50)
    description = models.CharField(null=True, max_length=50)
    price = models.FloatField(null=True, max_length=15)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    picture = models.ImageField(upload_to='car_pics/', null=True, blank=True)

    def __str__(self):
        return self.name
