#Run the OCR workflow
import read_specimen_text
import improved_crop
import cv2
import ocr_match_taxonomy
import os


def get_OCR_text(images_list):
    #param: list of images for OCR treatment
    #returns a list of lists (records) for further API lookups
    records = []
    print('images list == ', images_list)
    for key in images_list:
        img_path = images_list[key]
        img_name = key
        print('path: {} and name: {}'.format(img_path, img_name))
        img = cv2.imread(img_path)
        res = read_specimen_text.execute_image_label_vision(img)
        ocr_text = res[0]
        records.append(ocr_text)
        print("List of OCR'ed text: ", records)

    return records

##print statements for checking OCR result
cropped_imgs = improved_crop.exe_cropping('C:/python_dassco/Specimens_OCR/specimen_images',
                                               'C:/python_dassco/Specimens_OCR/cropped_images')

print('cropped imagesssssss: ', cropped_imgs)
OCR_treated_text = get_OCR_text(cropped_imgs)
for elem in OCR_treated_text:
    print('OCR text', elem , '\n')

##end##

candidates = OCR_treated_text
print('Google Vision api call res: ', candidates)

tax_res = []
for elem in candidates:
    res = ocr_match_taxonomy.look_up_species_names(elem)
    cleaned_res = ocr_match_taxonomy.check_for_api_cache_issues(res)
    tax_res.append(cleaned_res)

for j in tax_res: print('Submitted candidate string /{}/ ='.format(j[0]['submitted_string']), j)



