from __future__ import unicode_literals
from django.db import models 


# Create your models here.

class Main(models.Model):
    name= models.CharField(max_length=40)
    about= models.TextField()
    fc= models.CharField(default="-", max_length=40)
    tw= models.CharField(default="-", max_length=40)
    ins= models.CharField(default="-", max_length=40)
    tell= models.CharField(default="-", max_length=40)
    link= models.CharField(default="-", max_length=40)


    set_name= models.CharField(default="-", max_length=40)


    def __str__(self):
        return self.set_name +" | " +  str(self.pk)
    
    

    