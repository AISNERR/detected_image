from django.urls import path

from   images.views import *

urlpatterns = [
    path('images_gallery/', ImageCreateAPIView.as_view(), name="photo-gallery-list-create"),
]