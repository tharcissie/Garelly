from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_location(cls, pk, value):
        cls.objects.filter(pk=pk).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

  
class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to = 'articles/', null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=40, default='admin')

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    @classmethod
    def search_by_category(cls,category):
        image = cls.objects.filter(category__name__icontains=category)
        return image

    @classmethod
    def filter_by_location(cls, location):
        image = Image.objects.filter(location__name=location).all()
        return image

    @classmethod
    def update_image(cls, pk, value):
        cls.objects.filter(pk=pk).update(image=value)

    @classmethod
    def get_image_by_pk(cls, pk):
        image = cls.objects.filter(pk=pk).all()
        return image

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['date']