from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

  
class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField(max_length=255)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
