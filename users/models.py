from django.db import models
from django.contrib.auth.models import AbstractBaseUser

ROLE_CHOICES = (
    ("passenger","passenger"),
    ("operator","operator"),
)

# Create your models here.
class SUser(AbstractBaseUser):
    first_name = models.CharField(max_length=100,blank=False,null=False,verbose_name=" First Name ")
    last_name = models.CharField(max_length=150,blank=False,null=False,verbose_name=" Last Name ")
    email = models.EmailField(blank=False,null=False,unique=True,verbose_name=" Email Adress")
    national_id = models.CharField(max_length=10,blank=False,null=False,unique=True,verbose_name=" National ID")
    passport_id = models.CharField(max_length=8,blank=True,null=True,unique=True,verbose_name=" Passport ID")
    phone_number = models.CharField(max_length=11,blank=False,null=False,unique=True,verbose_name=" Phone Number")
    role = models.CharField(max_length=100,blank=False,null=False,verbose_name=" Role",choices=ROLE_CHOICES,default="passenger")

    def __str__(self):
        return self.first_name , self.last_name , self.national_id , self.email
    

