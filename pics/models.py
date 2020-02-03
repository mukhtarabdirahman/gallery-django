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
    image = models.ImageField(upload_to ='today-pics/')
    image_name = models.CharField(max_length =60)
    image_description = models.TextField()
    location = models.ForeignKey(Location)
    category= models.ForeignKey(Category)
    
    @classmethod
    def search_by_title(cls,search_term):
        pics = cls.objects.filter(title__icontains=search_term)
        return pics