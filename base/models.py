from django.db import models

# Create your models here.
class About(models.Model):
    
    description = models.TextField()
    image = models.ImageField(upload_to= 'Img/about')

class Services(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    image = models.ImageField( upload_to='Img/services')

class Testimonial(models.Model):
    name = models.CharField( max_length=50)
    position = models.CharField(max_length=50)
    description = models.TextField()
    
