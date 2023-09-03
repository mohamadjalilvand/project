from __future__ import unicode_literals
from django.db import models

    



# Create your models here.

class News(models.Model):
    name= models.CharField(max_length=40)
    short_txt= models.TextField()
    body= models.TextField()
    date= models.CharField(max_length=12)
    writer= models.TextField()


    def __str__(self):
        return self.name
    
    

    