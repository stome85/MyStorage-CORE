from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    description = models.CharField(
        max_length=250,
        blank=False,
        null=False
    )
    price = models.FloatField(
        blank=False,
        null=False
    )
    amount = models.IntegerField(
        blank=False,
        null=False
    )
    image = models.CharField(
        max_length=50,
        blank=True
    )

    def __str__(self):
        return self.name


class Sale(models.Model):
    pass


class ItemsSold(models.Model):
    pass
