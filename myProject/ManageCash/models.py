from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class AddCash(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.source} - {self.amount}"

class Expense(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"
