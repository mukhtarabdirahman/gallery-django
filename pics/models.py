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
        pics = cls.objects.filter(image_name__icontains=search_term)
        return pics
    
    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result
    
    def save_image(self):
        self.save()
    