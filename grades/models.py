from django.db import models

class Student(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )

    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    is_best = models.BooleanField(default=False)

    def __str__(self):
        return self.name
