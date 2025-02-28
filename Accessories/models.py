from django.db import models

class accessories(models.Model):
    CATEGORY_CHOICES = [
        ('jewelry', 'Jewelry'),
        ('bags', 'Bags'),
        ('hats', 'Hats'),
        ('belts', 'Belts'),
        ('sunglasses', 'Sunglasses'),
        ('watches', 'Watches'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='accessories/')
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

