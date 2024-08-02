from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'classes'

class Student(models.Model):
    class_number= models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.class_name.name})"