from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Department(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Attendance(models.Model):
    employee_name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.employee_name
