from django.db import models
from django.utils import timezone

# Create your models here.
class Expense(models.Model):
    title = models.CharField(max_length= 100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

