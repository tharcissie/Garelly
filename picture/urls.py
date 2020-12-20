from django.urls import path
from .views import home, location, search, details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name = 'home'),
    path('search/', search, name = 'search'),
    path('location/<location>/', location, name = 'location'),
    path('details/<int:pk>/', details, name = 'details')
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
