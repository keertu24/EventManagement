from django.core.exceptions import ValidationError
from django.db import models
import re



# Create your models here.
class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=30,unique=True)
    music_choice = models.IntegerField(default=0,null=True)
    food_choice = models.IntegerField(default=0,null=True)
    decor_choice = models.IntegerField(default=0,null=True)
    light_choice = models.IntegerField(default=0,null=True)
    stage_choice = models.IntegerField(default=0,null=True)
    
class UserProfile(models.Model):
    u_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=30,unique=True)
    user_mbl_no=models.CharField(max_length=60)
    user_dob=models.DateField()
    user_gender=models.CharField(max_length=30)
    user_image=models.URLField(null=True)

    

    def __str__(self):
        return self.user_name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=30)
    name=models.CharField(max_length=70)
    mbl_no=models.CharField(max_length=70)
    email=models.CharField(max_length=70)
    date=models.DateField()
    time=models.CharField(max_length=70)
    est_people=models.IntegerField()
    venue=models.CharField(max_length=70)
    venue_address=models.CharField(max_length=300)
    venue_pin=models.CharField(max_length=70)
    est_cost=models.IntegerField()
    invite_image=models.URLField()
    order_items=models.TextField(default='')

    def __str__(self):
        return self.user_name