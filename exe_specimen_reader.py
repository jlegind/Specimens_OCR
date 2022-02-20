import read_specimen_text as rst
import cv2_crawl_and_crop
import cv2


cropped_imgs = cv2_crawl_and_crop.exe_cropping('/home/stoffer/Pictures/images_for_pipeline')
print('¤', cropped_imgs)
# image = cv2.imread("specimen_images/majalis.png")
#
def get_OCR_text(images_list):
    #param: list of images for OCR treatment
    #returns a list of lists (records) for further API lookups
    records = []
    for key in cropped_imgs:
        img_path = cropped_imgs[key]
        print("image path == ", img_path)
        img_name = key
        img = cv2.imread(img_path)
        res = rst.execute_image_label_vision(img)
        print("OCR'ed text: ", res[0])
        cv2.imshow('input image {}-'.format(img_name), img)
        cv2.waitKey(0)
    #
        labels_list = res[0].split('|')
    #
        print("labels??", type(labels_list), labels_list)
        records.append(labels_list)
    return records

r2 = get_OCR_text(cropped_imgs)
print("get_CR_text out: ", r2)

