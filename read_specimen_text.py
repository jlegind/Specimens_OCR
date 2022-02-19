##Module for connecting image to Google Cloud Vision in order to obtain text in image.
##Author: Jan K. Legind
## Hat tip : rikvikmath
import os
from google.cloud import vision
import cv2


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "your_GCV_token.json"
client = vision.ImageAnnotatorClient()

def convert_to_GV_client_format(image):
    #image must be cv2.imread()
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    success, encoded_image = cv2.imencode('.jpg', img)
    roi_image = encoded_image.tobytes()
    roi_image = vision.Image(content=roi_image)
    response = client.text_detection(image=roi_image)
    return response

##################
# string processing of GCV text
##################

def parse_annotation_object(annotation_object):
    '''Pull out the label text and convert it to a text string for further processing'''
    labels = annotation_object.text_annotations[0].description

    tt = []
    [tt.append(elem) for elem in labels]

    agg = []
    listToStr = ''.join([str(elem) for elem in tt])

    for j in listToStr:
        if j == '\n':
            agg.append('|')
        else:
            agg.append(j)

    str_agg = ''.join([str(elem) for elem in agg])
    return str_agg

def execute_image_label_vision(input_img):
    #input image must by cv2.imread()
    #Returns tuple containing the OCR text and the cropped input image
    annotation = convert_to_GV_client_format(input_img)
    res = parse_annotation_object(annotation)
    return res, input_img