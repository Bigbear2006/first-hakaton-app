from django.db import models

class Product(models.Model):
    name = models.TextField()
    price = models.TextField()
    about_info = models.TextField()
    def __str__(self):
        return self.name

# Create your models here.
