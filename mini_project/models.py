from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Cat(models.Model):
    name = models.CharField(max_length=25)
    favorite_food = models.CharField(max_length=25)
    loves_pets = models.CharField(max_length=25)
    photo_url = models.TextField()
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE, related_name='comments')

    def __str__ (self):
        return self.author