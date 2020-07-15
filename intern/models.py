from django.db import models

# Create your models here.

class Destination2(models.Model):
    First_name=models.CharField(max_length=100)
    Middle_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    Company_name=models.CharField(max_length=100)
    Mobile_Number=models.IntegerField()
    Email=models.EmailField(max_length=100)
    Date_of_Birth=models.DateField(max_length=100)
    Pan_Card=models.CharField(max_length=100)
    Pin_Code=models.IntegerField()
    District=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Adhaar_Card=models.ImageField(upload_to='pics')
    Pan_Card=models.ImageField(upload_to='pics')

