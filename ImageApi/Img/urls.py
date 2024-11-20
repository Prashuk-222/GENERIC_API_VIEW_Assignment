from django.urls import path
from .views import ImageListCreateAPIView, ImageRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('images/', ImageListCreateAPIView.as_view(), name='image-list-create'),
    path('images/<int:pk>/', ImageRetrieveUpdateDestroyAPIView.as_view(), name='image-detail'),
]
