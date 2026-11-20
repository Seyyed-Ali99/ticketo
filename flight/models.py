from django.db import models
from users.models import SUser

# Create your model

class Airport(models.Model):
    name = models.CharField(max_length=250,blank=False,null=False,unique=True,verbose_name=" Name ")
    city = models.CharField(max_length=250,blank=False,null=False,verbose_name=" City ")
    country = models.CharField(max_length=250,blank=False,null=False,verbose_name=" Country ")
    code = models.CharField(max_length=3,blank=False,null=False,unique=True,verbose_name=" Airport Code",default="000")

    def __str__(self):
        return f"{self.name} , {self.city}"


class Airline(models.Model):
    name = models.CharField(max_length=150,blank=False,null=False,unique=True,verbose_name=" Name ")
    code = models.CharField(max_length=4,blank=False,null=False,unique=True,verbose_name=" Code ",default="0000")

    def __str__(self):
        return f"{self.name} , {self.code}" 


class Flight(models.Model):
    flight_num = models.CharField(max_length=9,blank=False,null=False,unique=True,default="000000000",verbose_name=" Flight Number ")
    airline = models.ForeignKey(Airline,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Airline ")
    origin = models.ForeignKey(Airport,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Origin ",related_name="origin_flight")
    destination = models.ForeignKey(Airport,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Destination ",related_name="destination_flight")
    board_time = models.DateTimeField(blank=False,null=False,unique=True,verbose_name=" Board Time ")
    arrival_time = models.DateTimeField(blank=False,null=False,unique=True,verbose_name=" Arrival Time ")
    price = models.IntegerField(blank=False,null=False,verbose_name=" Price ")
    capacity = models.IntegerField(blank=False,null=False,verbose_name=" Capacity ")
    airplane_model = models.CharField(max_length=50,null=False,blank=False,verbose_name="Airplane Model",default="Boeing-737")

    def __str__(self):
        return f"{self.flight_num} , {self.airline.name} , {self.origin.city} , {self.destination.city} "


STATUS_CHOICES = [
    ("pending","pending"),
    ("canceled","canceled"),
    ("ordered","ordered")
]



class Ticket(models.Model):
    passenger = models.ForeignKey(SUser,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Passenger ")
    flight = models.ForeignKey(Flight,on_delete=models.DO_NOTHING,blank=False,null=False,verbose_name=" Flight ")
    # seat_num = models.IntegerField(blank=False,null=False,unique=True,verbose_name=" Seat Number ")
    booking_date = models.DateTimeField(blank=True,null=True,verbose_name=" Booking Date ")
    status = models.CharField(max_length=100,blank=False,null=False,choices=STATUS_CHOICES,verbose_name=" Status ",default="pending")
    amount = models.IntegerField(null=False,blank=False,verbose_name="Amount",default=1)

    def __str__(self):
        return f"{self.passenger.first_name} , {self.passenger.last_name} , {self.flight}" 



