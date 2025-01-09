from django.db import models

# Create your models here.
class Bus(models.Model):
    bus_number = models.CharField(max_length=10, unique=True)
    
    stops = models.JSONField()

    def __str__(self):
        return self.bus_number