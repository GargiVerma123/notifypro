# leads/models.py
from django.db import models

class Lead(models.Model):
    customer_id = models.CharField(max_length=100, primary_key=True)  # Use a unique ID for the lead
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    summary = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('new', 'New'),
        ('contacted', 'Contacted'),
        ('converted', 'Converted'),
        ('closed', 'Closed'),
    ])

    def __str__(self):
        return self.name
