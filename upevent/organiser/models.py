import email
from turtle import title
from django.db import models

# Create your models here.
# model to collect your info and query
class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

# model to maintain news section 
class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='organiser/images', default="")
    desc = models.TextField(max_length=5000, default="" )


    def __str__(self):
        return self.title

class Organiser(models.Model):
    Type_choice=(
        ('FOOD','FOOD'),
        ('DECORATION','DECORATION'),
        ('MUSIC','MUSIC'),
        ('LIGHTING','LIGHTING'),
        ('STAGE PROGRAM','STAGE PROGRAM')
    )
    org_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    type_of_work=models.CharField(max_length=30,choices=Type_choice,default='MUSIC')
    date_of_join = models.DateField()
    User_email  = models.EmailField(max_length=70,unique=True)
    mobile_no= models.CharField(max_length=50,unique=True)
    address = models.TextField(max_length=300, default="" )
    password=models.CharField(max_length=50)


    def __str__(self):
        return self.username

    

    