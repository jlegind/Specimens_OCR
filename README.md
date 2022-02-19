# Specimens_OCR
Pipeline for OCR'ing labels on specimen images.  
This is a work in progress and modules will be added 'on the go' 

## Steps

1. Obtain image with labels
2. Crop to label section of image - (cv2_crawl_and_crop.py)
3. OCR the cropped image to Google Cloud Vision API (or other OCR service) - (read_specimen_text.py)
4. Output is one or more text blocks
5. OCR output of interest:
   - species name
   - date
   - catalog number
   - institution name
   - collector name    
6. The text tokens could be run against a look-up service such as the GBIF taxonomy API to determine if the text block contains a species name.
    The institution name might be determined by testing the text against the GBIF GRSCICOL API service.

## The CV2_specimen_OCR script
This script conforms to item 2 in the list above. The purpose is to acquire the part of the image where labels or text is stored.  
There is a certain assumption built into the script and that is that the labels are situated at the bottom part of the specimen image. This functionality will be updated.


The _crawl_dir_for_files()_ function returns a dictionary that is consumed in the for loop. Here each image is put through the _crop_bottom_half()_ function where each image is cropped. A ratio value of 2 will crop to the bottom half of the image. Chosing 1.5 will crop to the bottom half, and a high value will only shave off a few lines of pixels. 

## The read_specimen_text.py script
Here we have the first code that employs the Google Cloud Vision API service (GCV) for reading an image.  
The GCV client.text_detection() method returns a dictionary of text elements detected in the image.  
I think this code works well for specimen images where the images are cropped the region that contains labels.
The output of the _execute_image_label_vision()_ function is a list of the   
```
['CLF104120', 'HERBIERS UNIVERSITAIRES DE CLERMONT-FERRAND CLF104120.', 'Dactylorhiza maculata', '(L.) SOÓ', 'subsp. maculata', 'Famille Orchidaceae', 'Identification Thébaud G.', 'Récolteur Thomas M.', 'Date 2012', 'Date 6/7/2012', 'Pays France', 'Départerment Puy-de-Dôme', 'Commune Le Monestier', 'Virennes (Le Monestier, 63), PSET n°2.', 'note', 'RECOLNAT', '']
```
The next step is to extract text pieces that are species names...