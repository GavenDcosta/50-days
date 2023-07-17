from django.db import models

# Create your models here.

class Attribute(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.name
