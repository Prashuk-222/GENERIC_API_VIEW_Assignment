from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer
from .utils import fetch_image, calculate_md5, calculate_phash

class ImageListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def perform_create(self, serializer):
        image_url = self.request.data.get('image_url')
        image = fetch_image(image_url)
        md5_hash = calculate_md5(image)
        phash = calculate_phash(image)
        serializer.save(md5_hash=md5_hash, phash=phash)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        return response

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
