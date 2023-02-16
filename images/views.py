from .models import Image
from rest_framework import generics
from .serializers import  ImageCreate, ImageGet


class ImageCreateAPIView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
     
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ImageGet
        return ImageCreate

    def get_queryset(self):
        queryset = super(ImageCreateAPIView, self).get_queryset()
        return queryset  