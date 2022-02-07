import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

path = "/home/stoffer/Pictures/images_for_pipeline/"
image = cv2.imread(path + "lomarinopsis.png")
print('img shape', image.shape)
# cv2.imshow('orig', image)
# cv2.waitKey(0)
h = image.shape[0]
w = image.shape[1]

def crawl_dir_for_files(dir):
    img_dict = {}
    for im in os.listdir(dir):
        f = os.path.join(dir, im)
        if os.path.isfile(f):
            print(f)
            img_dict[im]=f
    return img_dict

def crop_bottom_half(image, ratio):
    cropped_img = image[int(image.shape[0]/ratio):int(image.shape[0])]
    return cropped_img

mages = crawl_dir_for_files("/home/stoffer/Pictures/images_for_pipeline")
print('MAGES ^', mages)
for key in mages:
    print('the key/name=', key)
    print('the image path=', mages[key])
    img_path = mages[key]
    img_name = key
    img = cv2.imread(img_path)
    cropped = crop_bottom_half(img, 2)
    print('cropped img dimensions: ', cropped.shape)
    os.chdir('/home/stoffer/Pictures/output')
    print('2cropped_{}'.format(img_name))
    cv2.imwrite('cropped_{}.png'.format(img_name), cropped)

    cv2.imshow(img_name, cropped)
    cv2.waitKey(0)

