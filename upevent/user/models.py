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
    
