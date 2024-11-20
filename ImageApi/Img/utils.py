import requests
from PIL import Image
import hashlib
import imagehash
from io import BytesIO

def fetch_image(url):
    response = requests.get(url)
    response.raise_for_status()

    if 'image' not in response.headers.get('Content-Type', ''):
        raise ValueError("URL does not point to an image")

    try:
        image = Image.open(BytesIO(response.content))
        image.verify()  
        image = Image.open(BytesIO(response.content)) 
        return image
    except Exception as e:
        raise ValueError(f"Failed to process image from URL: {e}")

def calculate_md5(image):
    md5 = hashlib.md5()
    md5.update(image.tobytes())
    return md5.hexdigest()

def calculate_phash(image):
    return str(imagehash.phash(image))
