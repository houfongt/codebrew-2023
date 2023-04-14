import io
import os

from google.cloud import vision
from google.cloud.vision_v1 import types
import requests

# Set the environment variable for the service account key file
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/macbook/Keys/codebrew-2023-01234ee1946e.json'

# Initialize the client
client = vision.ImageAnnotatorClient()
image = vision.Image()

# Define the URL of the JPEG image
image_url = 'https://cdn.britannica.com/17/196817-050-6A15DAC3/vegetables.jpg'

response = client.annotate_image({
 'image': {'source': {'image_uri': image_url}},
 'features': [{'type_': vision.Feature.Type.OBJECT_LOCALIZATION, 'max_results': 20},
 {'type_': vision.Feature.Type.DOCUMENT_TEXT_DETECTION}
  ]
})

lo_annotations = response.localized_object_annotations
for obj in lo_annotations:
    print(obj.name)