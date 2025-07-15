from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    address=models.TextField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

