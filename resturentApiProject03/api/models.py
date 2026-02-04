from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    restaurant_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    total_amount = models.IntegerField()

    def __str__(self):
        return self.customer_name


class Table(models.Model):
    table_number = models.IntegerField()
    seats = models.IntegerField()

    def __str__(self):
        return str(self.table_number)
