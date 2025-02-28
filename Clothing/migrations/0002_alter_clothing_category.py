# Generated by Django 5.1.6 on 2025-02-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clothing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothing',
            name='category',
            field=models.CharField(choices=[('TS', 'T-Shirt'), ('SH', 'Shirt'), ('JK', 'Jacket'), ('PN', 'Pants'), ('SW', 'Sweater'), ('DR', 'Dress'), ('HD', 'Hoodies'), ('TR', 'Trousers')], max_length=2),
        ),
    ]
