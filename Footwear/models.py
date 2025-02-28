from django.db import models

# Create your models here.

FOOTWEAR_CATEGORIES = [
    ('Sneakers', 'Sneakers'),
    ('Formal', 'Formal'),
    ('Boots', 'Boots'),
    ('Sandals', 'Sandals'),
    ('Sports', 'Sports'),
    ('Casual', 'Casual'),
    ('Heels', 'Heels'),
    ('Slippers', 'Slippers'),
]

# Size choices (can be expanded as needed)
SIZE_CHOICES = [(str(size), str(size)) for size in range(5, 13)]  # US Sizes 5-12

# Color choices
COLOR_CHOICES = [
    ('Black', 'Black'),
    ('White', 'White'),
    ('Red', 'Red'),
    ('Blue', 'Blue'),
    ('Green', 'Green'),
    ('Brown', 'Brown'),
    ('Grey', 'Grey'),
    ('Yellow', 'Yellow'),
]

class footwear(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the footwear")
    brand = models.CharField(max_length=50, help_text="Brand of the footwear")
    category = models.CharField(max_length=20, choices=FOOTWEAR_CATEGORIES, help_text="Type of footwear")
    size = models.CharField(max_length=5, choices=SIZE_CHOICES, help_text="Size of the footwear")
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, help_text="Color of the footwear")
    material = models.CharField(max_length=50, help_text="Material used (e.g., Leather, Canvas, Synthetic)")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    stock = models.PositiveIntegerField(help_text="Available stock")
    description = models.TextField(blank=True, help_text="Detailed description of the footwear")
    image = models.ImageField(upload_to='footwear_images/', blank=True, null=True, help_text="Upload product image")
    date_added = models.DateTimeField(auto_now_add=True, help_text="Date when footwear was added")

def __str__(self):
        return f"{self.brand} {self.name} ({self.size})"