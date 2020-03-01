from django.db import models


class Category(models.Model):
    image_category = models.CharField(max_length=20)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
    @classmethod
    def get_cat_by_ID(cls, id):
        cat = Category.objects.get(pk=id)
        return cat
    
    def update_cat(self, updated_category):
        self.image_category = updated_category
        self.save()
    class Meta:
        ordering =['image_category']
           
class Location(models.Model):
    image_location = models.CharField(max_length=20)
    
    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()
    @classmethod
    def get_loc_by_ID(cls, id):
        location = Location.objects.get(pk=id)
        return location
    
    def update_loc(self,updated_pinpoint):
        self.image_location = updated_pinpoint
        self.save()
    class Meta:
        ordering = ['image_location']
    
class Image(models.Model):
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    
        
    @classmethod  
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image
        
    def update_img(self,image_name, image_description):
        self.image_name = image_name
        self.image_description = image_description
        self.save()
    
    
    @classmethod
    def search_by_category(cls, search_word):
        images = cls.objects.filter(category__image_category__icontains=search_word)
        return images
    
    @classmethod
    def filter_by_location(cls, loc):
        images_loc = cls.objects.filter(location__id=loc)
        return images_loc
    @classmethod
    def get_images(cls):
        all_images = cls.objects.all()
        return all_images 
        

    
        
        
    

