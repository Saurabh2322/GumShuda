from django.contrib import admin
from django.urls import path
from missingperson.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Add your views here
# Example: from .views import locations

urlpatterns = [
    path('', home, name='home'),
    path('detect/', detect, name='detect'),
    path('surveillance/', surveillance, name='surveillance'),
    path('register/', register, name='register'),
    path('missing/', missing, name='missing'),
    path('delete/<int:person_id>/', delete_person, name='delete_person'),
    path('update/<int:person_id>/', update_person, name='update_person'),
    path('location/', location, name='location'),  # Add this line for locations
    path('admin/', admin.site.urls),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
