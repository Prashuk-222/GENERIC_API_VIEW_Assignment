from django.db import models

class Image(models.Model):
    image_url = models.URLField()
    md5_hash = models.CharField(max_length=32)
    phash = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image_url
