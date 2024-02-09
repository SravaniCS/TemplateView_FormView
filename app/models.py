from django.db import models

# Create your models here.

class Company(models.Model):
    cname=models.CharField(max_length=100)
    cloc=models.CharField(max_length=100)

    def __str__(self):
        return self.cname