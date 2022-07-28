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
    desc = models.CharField(max_length=5000, default="")


    def __str__(self):
        return self.title
