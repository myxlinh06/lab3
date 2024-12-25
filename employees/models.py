from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Thêm các trường khác tùy nhu cầu

    def __str__(self):
        return self.name