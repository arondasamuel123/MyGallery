from django.db import models


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
class Category(models.Model):
    category = models.CharField(max_length=20)
    
class Location(models.Model):
    loction = models.CharField(max_length=20)
