from rest_framework import serializers

from  images.models import Image


class ImageCreate(serializers.ModelSerializer):
     
    class Meta:
        model = Image
        fields = ['id', 'title', 'image']

    def create(self, validated_data):
        validated_data["created_by"] = self.context['request'].user
        return super(ImageCreate, self).create(validated_data)

    def update(self, instance, validated_data):
        return super(ImageCreate, self).update(instance, validated_data)


class  ImageGet(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

