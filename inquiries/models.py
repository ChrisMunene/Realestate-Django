from django.db import models
from django.utils import timezone

# Create your models here.
class Inquiry(models.Model):
    listing_name = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    user_id = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.name