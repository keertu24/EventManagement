from email.policy import default
from pyexpat import model
from django.db import models

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
    user_mbl_no=models.CharField(max_length=60,unique=True)
    user_dob=models.DateField()
    user_gender=models.CharField(max_length=30)
    user_image=models.URLField(null=True)

    def __str__(self):
        return self.user_name