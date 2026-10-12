from django.db import models
from django.contrib.auth.models import AbstractBaseUser,AbstractUser

ROLE_CHOICES = (
    ("passenger","passenger"),
    ("operator","operator"),
)

# Create your models here.
class SUser(AbstractUser):
    first_name = models.CharField(max_length=100,blank=False,null=False,verbose_name=" First Name ")
    last_name = models.CharField(max_length=150,blank=False,null=False,verbose_name=" Last Name ")
    email = models.EmailField(blank=False,null=False,unique=True,verbose_name=" Email Adress")
    national_id = models.CharField(max_length=10,blank=False,null=False,unique=True,verbose_name=" National ID")
    passport_id = models.CharField(max_length=8,blank=True,null=True,unique=True,verbose_name=" Passport ID")
    phone_number = models.CharField(max_length=11,blank=False,null=False,unique=True,verbose_name=" Phone Number")
    role = models.CharField(max_length=100,blank=False,null=False,verbose_name=" Role",choices=ROLE_CHOICES,default="passenger")

    password = models.CharField(verbose_name=" Password",blank=False,null=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='s_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='s_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.first_name , self.last_name , self.national_id , self.email , self.passport_id , self.phone_number , self.role 
    

