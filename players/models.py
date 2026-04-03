from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    dateJoined = models.DateField()
    position = models.CharField(max_length=50)
    salary_payment = models.DecimalField(max_digits=10, decimal_places=2)
    contactPerson = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.position})"
