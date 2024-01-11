from django.db import models

class Category(models.Model):
    name = models.fields.CharField(null=True, max_length=50)

    def __str__(self):
        return self.name