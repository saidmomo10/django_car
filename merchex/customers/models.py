from django.db import models

class Customer(models.Model):
    firstname = models.fields.CharField(null=True, max_length=50)
    lastname = models.fields.CharField(null=True, max_length=50)
    email = models.fields.CharField(null=True, max_length=50)
    phone = models.fields.FloatField(null=True, max_length=15)
    address = models.fields.CharField(null=True, max_length=50)
    # profile_picture = models.ImageField(upload_to='customer_profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.firstname
