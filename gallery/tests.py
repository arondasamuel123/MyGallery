from django.test import TestCase
from .models import Image, Category, Location

class ImageTestClass(TestCase):
    '''
    Test Class for Image model methods 
    '''
    def setUp(self):
        self.category_one = Category(image_category='Nature')
        self.location_one = Location(image_location='Rift Valley')
        self.image_one= Image(image_name= 'Mountains', image_description='Mountains in the distance', image='/path/image.png', category=self.category_one, location=self.location_one)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.image_one, Image))
        
    def test_save_image(self):
        self.category_one.save_category()
        self.location_one.save_location()
        self.image_one.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)
        
    def test_delete_image(self):
        self.category_one.save_category()
        self.location_one.save_location()
        self.image_one.save_image()
        self.image_one.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images)== 0)
        
    def test_get_image_by_id(self):
        self.category_one.save_category()
        self.location_one.save_location()
        self.image_one.save_image()
        images = Image.get_image_by_id(self.image_one.id)
    
    def test_update_image(self):
        self.category_one.save_category()
        self.location_one.save_location()
        self.image_one.save_image()
        self.image_one.get_image_by_id(self.image_one.id)
        self.image_one.update_img('Travel', 'Travelling in style')
        self.assertTrue(self.image_one.image_name=='Travel')
    
    def test_seach_by_cat(self):
        self.category_one.save_category()
        self.location_one.save_location()
        self.image_one.save_image()
        images = self.image_one.search_by_category('Nature')
        self.assertTrue(len(images)>0)
        
    def test_filter_by_loc(self):
        self.category_one.save_category()
        self.location_one.save_location()
        self.image_one.save_image()
        images = self.image_one.filter_by_location(self.location_one.id)
        self.assertTrue(len(images) > 0)
        
class CategoryTestClass(TestCase):
    '''
    Test Class for Category model methods
    '''
    def setUp(self):
        self.category = Category(image_category='Nature')
        
    
    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)> 0)
    
    def test_delete_category(self):
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)== 0)
        
    def test_update_category(self):
        self.category.save_category()
        category = self.category.get_cat_by_ID(self.category.id)
        category.update_cat('Food')
        self.assertTrue(category.image_category == 'Food')
        
        
class LocationTestClass(TestCase):
    '''
    Test Class for Location modal and methods
    '''
    def setUp(self):
        self.location = Location(image_location='Karen')
    
    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)
        
    def test_delete_location(self):
        self.location.save_location()
        self.location.delete_location()
        
        locations = Location.objects.all()
        self.assertTrue(len(locations)== 0)
        
    def test_update_location(self):
        self.location.save_location()
        location = self.location.get_loc_by_ID(self.location.id)
        location.update_loc('Westlands')
        self.assertTrue(location.image_location=='Westlands')
        
        
        
        
    
        
        
        
        
        
        
    
