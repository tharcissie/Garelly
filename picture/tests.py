
from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.

class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location.objects.create(name='Kigali')
        self.category = Category.objects.create(name='car')
        self.car= Image(name = 'car', description ='Muriuki', location = self.location, category = self.category)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.car,Image))

    def test_save_method(self):
        self.car.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

  