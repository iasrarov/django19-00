from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Myself(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

