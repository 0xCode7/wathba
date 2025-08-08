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


class Feedback(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Feedback from {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"