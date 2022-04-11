import cv2
import os
#package for extracting a part of an image , be it Left, Right, Top, Bottom

def crawl_dir_for_files(dir):
    # Returns a dictionary where the image name is the key and the value is the path to the image.
    img_dict = {}
    for im in os.listdir(dir):
        f = os.path.join(dir, im)
        if os.path.isfile(f):
            img_dict[im]=f
    return img_dict

def crop_LRTB(img_path, segment, percentage):
    #segment is which image part is requested Left, Right, Top, Bottom
    #percentage is how much of the image you wish to RETAIN. The rest to be cropped away (for example 33% would by the integer 33)
    img = cv2.imread(img_path)

    height, width, channels = img.shape
    to_pixel = percentage / 100
    cv2.imshow('original', img)
    cv2.waitKey(0)

    h_shear = int(width * to_pixel)
    #H_shear is for segmenting along horizontal direction
    #horizontal axis operations
    if segment == 'left':
        left = img[:, :h_shear]
        lh, lw, _ = left.shape
        return left

    if segment == 'right':
        right = img[:, h_shear:]
        return right

# this is vertical division

    v_shear =  int(height * to_pixel)

    if segment == 'top':
        top = img[:v_shear, :]
        return top

    if segment == 'bottom':
        bottom = img[v_shear:, :]
        bh, bw, _ = bottom.shape
        return bottom


images_dict = crawl_dir_for_files('/home/stoffer/specimen_ocr/Specimens_OCR/specimen_images')
print(images_dict)
output_dir = '/home/stoffer/specimen_ocr/Specimens_OCR/cropped_images'

#exe logic
def run_cropping_ops(images_dict, crop_amount = 33, crop_part='bottom', output_dir=''):
    #for driving the other functions
    #crop amount is the percentage of image remaining after crop operation
    for key in images_dict:
        img_path = images_dict[key]
        img_name = key
        print(f'img path:{img_path} + img name: {img_name}')
        img = cv2.imread(img_path)
        # cv2.imshow('to crop', img)
        # cv2.waitKey(0)
        shp = img.shape
        print(img_path, shp)

        crop_amount = crop_amount
        cropped = crop_LRTB(img_path, 'left', crop_amount)

        cv2.imshow('crop', cropped)
        cv2.waitKey(0)

        cropped_path = output_dir
        os.chdir(cropped_path)
        img_name = img_name.replace('.png', '')

        cv2.imwrite('{} cropped_{}_{}.png'.format(crop_part, crop_amount, img_name), cropped)
        print('end of ', img_path)

#
#run_cropping_ops(images_dict, crop_amount=50, crop_part='left', output_dir=output_dir)
#