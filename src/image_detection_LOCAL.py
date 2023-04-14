import io
import os

from google.cloud import vision
from google.cloud.vision_v1 import types
import requests

# Set the environment variable for the service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/macbook/Keys/codebrew-2023-01234ee1946e.json'

# Initialize the client
client = vision.ImageAnnotatorClient()

# # Define the path to the local JPEG file
image_path = '../src/assets/food_image_test.jpeg'

# Read the image file
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# Create a Vision API image object from the image data
image = types.Image(content=content)

# Perform label detection on the image
response = client.label_detection(image=image)
labels = response.label_annotations

# Print the labels
for label in labels:
    print(label.description)
    