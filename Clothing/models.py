from django.db import models

class clothing(models.Model):
    CATEGORY_CHOICES = [
        ('T-Shirt', 'T-Shirt'),
        ('Shirt', 'Shirt'),
        ('Jacket', 'Jacket'),
        ('Pants', 'Pants'),
        ('Sweater', 'Sweater'),
        ('Dress', 'Dress'),
        ('Hoodies', 'Hoodies'),
        ('Trousers', 'Trousers')
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)  # Increased max_length
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='clothing_images/')

    def __str__(self):
        return self.name


