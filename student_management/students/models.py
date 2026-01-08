from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50) 
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student_name = models.CharField(max_length=255)
    courses = models.TextField() 
    payment_method = models.CharField(max_length=50, default="bkash")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.student_name} - {self.timestamp.date()}"