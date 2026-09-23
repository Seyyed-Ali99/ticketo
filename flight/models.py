from django.db import models

# Create your models here.

class Airport(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False,unique=True,verbose_name=" Name ")
    city = models.CharField(max_length=250,blank=False,null=False,unique=True,verbose_name=" City ")
    country = models.CharField(max_length=250,blank=False,null=False,unique=True,verbose_name=" Country ")
    code = models.CharField(max_length=10,blank=False,null=False,unique=True,verbose_name=" Port Code ")

    def __str__(self):
        return self.name , self.city , self.country , self.code


class Airline(models.Model):
    pass

class Flight(models.Model):
    pass


class Ticket(models.Model):
    pass



