from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('ПОДУШКА', 'Подушки'),
        ('МАТРАС', 'Матрасы'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='')
    description = models.TextField(max_length=1000, default='')
    photo = models.ImageField(max_length=255, null=False, blank=True)

