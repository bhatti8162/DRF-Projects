from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()

    def __str__(self):
        return self.name
