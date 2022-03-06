from django.db import models


# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=25)
    lname=models.CharField(max_length=30)
    email=models.EmailField(max_length=250)

    class Meta:
        db_table="Emp"



