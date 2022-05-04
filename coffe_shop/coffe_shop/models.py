from django.db import models


class Drink(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price_tall = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_grande = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    price_venti = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return self.name
