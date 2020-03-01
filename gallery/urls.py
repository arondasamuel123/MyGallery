from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views 


urlpatterns  = [
    path('', views.index, name='index'),
    path('search/', views.search_images, name='search_images'),
    path('filter/<int:img_location>', views.filter_by_loc, name='filter_loc'),
    path('image/<int:id>', views.specific_image, name='specific_image')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)