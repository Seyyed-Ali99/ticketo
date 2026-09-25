from django.db import models
from users.models import SUser

# Create your models here.

class Airport(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False,unique=True,verbose_name=" Name ")
    city = models.CharField(max_length=250,blank=False,null=False,unique=True,verbose_name=" City ")
    country = models.CharField(max_length=250,blank=False,null=False,unique=True,verbose_name=" Country ")
    code = models.CharField(max_length=10,blank=False,null=False,unique=True,verbose_name=" Port Code ")

    def __str__(self):
        return self.name , self.city , self.country , self.code


class Airline(models.Model):
    name = models.CharField(max_length=150,blank=False,null=False,unique=True,verbose_name=" Name ")
    code = models.CharField(max_length=150,blank=False,null=False,unique=True,verbose_name=" Code ")

    def __str__(self):
        return self.name , self.code 


class Flight(models.Model):
    flight_num = id
    airline = models.ForeignKey(Airline,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Airline ")
    origin = models.ForeignKey(Airport,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Origin ")
    destination = models.ForeignKey(Airport,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Destination ")
    arrival_time = models.DateTimeField(blank=False,null=False,unique=True,verbose_name=" Arrival Time ")
    price = models.IntegerField(max_length=9,blank=False,null=False,verbose_name=" Price ")
    capacity = models.IntegerField(max_length=3,blank=False,null=False,verbose_name=" Capacity ")


STATUS_CHOICES = [
    ("pending","pending"),
    ("canceled","canceled"),
    ("ordered","ordered")
]



class Ticket(models.Model):
    passenger = models.ForeignKey(SUser,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Passenger ")
    flight = models.ForeignKey(Flight,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Flight ")
    seat_num = models.IntegerField(max_length=3,blank=False,null=False,unique=True,verbose_name=" Seat Number ")
    booking_date = models.DateTimeField(blank=False,null=False,verbose_name=" Booking Date ")
    status = models.CharField(max_length=100,blank=False,null=False,choices=STATUS_CHOICES,verbose_name=" Status ")



