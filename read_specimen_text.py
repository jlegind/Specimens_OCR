##Module for connecting image to Google Cloud Vision in order to obtain text in image.
##Author: Jan K. Legind
## Hat tip : rikvikmath
import os
from google.cloud import vision
from PIL import Image
import cv2


img = cv2.imread('specimen_images/dacty.png')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "your_GCV_token.json"
client = vision.ImageAnnotatorClient()

def convert_to_GV_client_format(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    success, encoded_image = cv2.imencode('.jpg', img)
    roi_image = encoded_image.tobytes()
    roi_image = vision.Image(content=roi_image)
    response = client.text_detection(image=roi_image)
    return response
#
img_for_GCV = convert_to_GV_client_format(img)

for word in img_for_GCV.text_annotations:
    d = {'text': word.description}
    print(d)

img = Image.open("specimen_images/dacty.png")

