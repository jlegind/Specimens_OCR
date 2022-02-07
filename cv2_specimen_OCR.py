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

def crop_bottom_half(image):
    cropped_img = image[int(image.shape[0]/2):int(image.shape[0])]
    return cropped_img

mages = crawl_dir_for_files("/home/stoffer/Pictures/images_for_pipeline")
print('MAGES ^', mages)
for key in mages:
    print('the key/name=', key)
    print('the image path=', mages[key])
    img_path = mages[key]
    img_name = key
    img = cv2.imread(img_path)
    cropped = crop_bottom_half(img)
    os.chdir('/home/stoffer/Pictures/output')
    print('cropped_{}'.format(img_name))
    cv2.imwrite('cropped_{}.png'.format(img_name), cropped)

    cv2.imshow(img_name, cropped)
    cv2.waitKey(0)


###remember the imwrite() part!!!!!!!
# crop_img = crop_bottom_half(image)
# cv2.imshow('cropped sector', crop_img)
# cv2.imwrite(path+'/output/cropped_img2.png', crop_img)
# cv2.waitKey(0)



# cv2.rectangle(image, (w, mhigh), (0, h), green, 3)
# cv2.imshow("Canvas", image)
# cv2.waitKey(0)
# white = [255,255,255]

#MAKE WHITE BORDER vv
# constant= cv2.copyMakeBorder(image,20,20,20,20,cv2.BORDER_CONSTANT,value=white)
# cv2.imshow('output.png',constant)
# cv2.waitKey(0)





# froi = cv2.selectROI(image)
# print('the roi points', froi)
# cv2.imshow('orig', image)
# ROI = image[0:1000, 1350:450]
# cv2.imwrite('rectcut_out.png', ROI)

# cv2.waitKey(0)