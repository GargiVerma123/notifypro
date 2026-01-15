from django.db import models

# Customer model to store customer information (if not already defined)
class Customer(models.Model):
    customer_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Address choices for the drop-down menu in List model
class List(models.Model):
    ADDRESS_CHOICES = [
        ('hinjiwade', 'Hinjiwade'),
        ('wakad', 'Wakad'),
        ('ravet', 'Ravet'),
        ('punawale', 'Punawale'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    address = models.CharField(max_length=50, choices=ADDRESS_CHOICES)

    def __str__(self):
        return f"{self.customer.name} - {self.address}"
