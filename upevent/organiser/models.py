import email
from unicodedata import category
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
    news_title = models.CharField(max_length=50)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='organiser/images', default="")
    desc = models.TextField(max_length=5000, default="" )


    def __str__(self):
        return self.news_title

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

class Service(models.Model):
    service_id=models.AutoField(primary_key=True)
    services=models.CharField(max_length=100)

    def __str__(self) :
        return self.services
    
    class Meta:
        ordering=['services']

class Event(models.Model):
    event_id=models.AutoField(primary_key=True)
    event_title=models.CharField(max_length=50,default="")
    category=models.ManyToManyField(Service)
    event_image=models.ImageField(upload_to='Event/images', default="")
    event_desc=models.TextField(max_length=300, default="" )
    
    def __str__(self) :
        return self.event_title

class Package(models.Model):
    Type_choice=(
        ('FOOD','FOOD'),
        ('DECORATION','DECORATION'),
        ('MUSIC','MUSIC'),
        ('LIGHTING','LIGHTING'),
        ('STAGE PROGRAM','STAGE PROGRAM')
    )
    package_id=models.AutoField(primary_key=True)
    package_title=models.CharField(max_length=50,default="")
    category=models.CharField(max_length=30,choices=Type_choice,default='MUSIC')
    package_image=models.ImageField(upload_to='Package/images', default="")
    package_desc=models.TextField(max_length=300, default="" )
    package_price=models.IntegerField(default=10000)

    def __str__(self) :
        return self.package_title


    