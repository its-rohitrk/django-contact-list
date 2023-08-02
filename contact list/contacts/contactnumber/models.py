from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length=400)
    relationship = models.CharField(max_length=100)
    enail = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.full_name