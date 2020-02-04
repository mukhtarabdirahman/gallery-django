from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length =30)

    
    def __str__(self):
        return self.location
    def save_location(self):
        self.save()
        
        
class Category(models.Model):
        category = models.CharField(max_length =30)
        def __str__(self):
            return self.category
    
class Image(models.Model):
    image = models.ImageField(upload_to ='today-search_results/')
    image_name = models.CharField(max_length =60)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category= models.ForeignKey(Category)
    
    
    @classmethod
    
    def search_by_image_name(cls,search_term):
        display = cls.objects.filter(category__category__icontains=search_term)
        return display
    
    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result
    
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item;
    @classmethod
    def update_image(cls,current_value,new_value):
        fetched_object = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return fetched_object
    @classmethod
    def filter_by_location(cls,location):
        filtered_result = cls.objects.filter(location__location_name__icontains=location)
        return filtered_result