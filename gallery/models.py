from django.db import models


class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete
        
    def get_image_by_id(self, image_id):
        self.objects.get(id= image_id)
        
    def search_image(self,search_term):
        images = self.objects.filter(category__icontains=search_term)
        return images
        
    def filter_by_loc(self, loc):
        image_loc = self.objects.filter(location= loc)
        
        
    
class Category(models.Model):
    category = models.CharField(max_length=20)
    
class Location(models.Model):
    loction = models.CharField(max_length=20)
