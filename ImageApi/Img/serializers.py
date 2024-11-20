from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_url', 'md5_hash', 'phash', 'created_at', 'updated_at']
        read_only_fields = ['md5_hash', 'phash']
