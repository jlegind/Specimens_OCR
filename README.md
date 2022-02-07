# Specimens_OCR
Pipeline for OCR'ing labels on specimen images 

## Steps

1. Obtain image with labels
2. Cropt to label section of image
3. OCR the cropped image to Google Cloud Vision API (or other OCR service)
4. Output is one or more text blocks
5. Analyze which block of text has the:
   - species name
   - date
   - catalog number
   - institution name
   - collector name  
   
6. The text tokens could be run against a look-up service such as the GBIF taxonomy API to determine if the text block contains a species name.
    The institution name might be determined by testing the text against the GBIF GRSCICOL API service.

