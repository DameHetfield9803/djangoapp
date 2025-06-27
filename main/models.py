from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.
class MenuItems(models.Model):
    id = models.IntegerField
    name = models.CharField(max_length=255)
    price = models.FloatField()
    

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField(validators=[MinValueValidator(1)],default=0)
    reservation_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=1024)