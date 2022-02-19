##Code for iterating over image files in a directory and cropping them (bottom up) by an arbitrary ratio

import cv2
import os

def crawl_dir_for_files(dir):
    # Returns a dictionary where the image name is the key and the value is the path to the image.
    img_dict = {}
    for im in os.listdir(dir):
        f = os.path.join(dir, im)
        if os.path.isfile(f):
            img_dict[im]=f
    return img_dict

def crop_bottom_half(image, ratio=2):
    #image: is the image object itself - cv2.imread() or similar
    #ratio:
    cropped_img = image[int(image.shape[0]/ratio):int(image.shape[0])]
    return cropped_img

def exe_cropping(path_to_input_specimen_images):
    #Runs the functions above and returns a dict with the cropped image addresses
    images_dict = crawl_dir_for_files(path_to_input_specimen_images)
    for key in images_dict:
        img_path = images_dict[key]
        img_name = key
        img = cv2.imread(img_path)
        cropped = crop_bottom_half(img, ratio=2)
        print('cropped img dimensions: ', cropped.shape)
        cropped_path = '/home/stoffer/OCR/Specimens_OCR/cropped_images'
        os.chdir(cropped_path)
        img_name = img_name.replace('.png', '')
        print('cropped_{}'.format(img_name)) #remove the suffix part as it is now redundant
        cv2.imwrite('cropped_{}.png'.format(img_name), cropped)

        cv2.imshow(img_name, cropped)

    cv2.waitKey(0)
    cropped_dict = crawl_dir_for_files(cropped_path)

    return cropped_dict




