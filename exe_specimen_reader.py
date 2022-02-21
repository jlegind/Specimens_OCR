#Run the OCR workflow
import read_specimen_text
import cv2_crawl_and_crop
import cv2
import ocr_match_taxonomy


def get_OCR_text(images_list):
    #param: list of images for OCR treatment
    #returns a list of lists (records) for further API lookups
    records = []
    for key in cropped_imgs:
        img_path = cropped_imgs[key]
        img_name = key
        img = cv2.imread(img_path)
        res = read_specimen_text.execute_image_label_vision(img)
        ocr_text = res[0]
        records.append(ocr_text)
        print("List of OCR'ed text: ", records)
        # cv2.imshow('input image {}-'.format(img_name), img)
        # cv2.waitKey(0)

        # print("labels??", type(labels_list), labels_list)
        # records.append(labels_list)
    return records
cropped_imgs = cv2_crawl_and_crop.exe_cropping('/home/stoffer/Pictures/images_for_pipeline')
print('type Cropped IMGES: ', type(cropped_imgs))
OCR_treated_text = get_OCR_text(cropped_imgs)
print("get_CR_text out: ", OCR_treated_text)

# for candidate in OCR_treated_text:
candidates = OCR_treated_text
print('Google Vision api call res: ', candidates)
# species_names = ocr_match_taxonomy.look_up_species_names(candidates)

# def obtain_
tax_res = []
for elem in candidates:
    res = ocr_match_taxonomy.look_up_species_names(elem)
    cleaned_res = ocr_match_taxonomy.check_for_api_cache_issues(res)
    tax_res.append(cleaned_res)
# conf = ocr_match_taxonomy.check_for_api_cache_issues(species_names)

for j in tax_res: print(j)
# print('\n GBIF Taxonomic lookup == ', tax_res)


