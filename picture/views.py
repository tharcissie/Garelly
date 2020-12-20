from django.shortcuts import render
from .models import Image, Location, Category
from django.http  import HttpResponse, Http404

# Create your views here.

def home(request):
    image = Image.objects.all()
    locations = Location.get_locations()
    category = Category.objects.all()
    context = {'image':image, 'locations': locations, 'category':category}
    return render(request, 'home.html', context )

def location(request, location):
    images = Image.filter_by_location(location)
    locations = Location.get_locations()
    category = Category.objects.all()
    context = {'images':images, 'locations': locations, 'category':category}
    return render(request, 'location.html', context)

def search(request):
    locations = Location.get_locations()
    category1 = Category.objects.all()
    if 'searchimage' in request.GET and request.GET["searchimage"]:
        category = request.GET.get("searchimage")
        images = Image.search_by_category(category)
        return render(request, 'search.html', {"images":images, 'locations': locations, 'category1':category1})
    else:
        return render(request, 'search.html', {'locations': locations,'category1':category1})

def details(request, pk):
    try:
        image = Image.objects.get(pk = pk)
    except DoesNotExist:
        raise Http404()
    return render(request,"details.html", {"image":image})


