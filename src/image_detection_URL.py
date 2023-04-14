import io
import os

from google.cloud import vision
from google.cloud.vision_v1 import types
import requests

# Set the environment variable for the service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/macbook/Keys/codebrew-2023-01234ee1946e.json'

# Initialize the client
client = vision.ImageAnnotatorClient()

# Define the URL of the JPEG image
image_url = 'https://www.snexplores.org/wp-content/uploads/2022/10/1440_SS_fruit_feat-1030x580.jpg'

# Download the image data from the URL
response = requests.get(image_url)
image_content = response.content

# Create a Vision API image object from the image data
image = types.Image(content=image_content)

# Perform label detection on the image
response = client.label_detection(image=image)
labels = response.label_annotations

# Print the labels
for label in labels:
    print(label.description)
