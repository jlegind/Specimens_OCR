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


specimen_images_dir = ''
images_dict = {}

# output_dir = 'cropped_images'


def crop_LRTB(img_path, segment, percentage):
    #segment is which image part is requested Left, Right, Top, Bottom
    #percentage is how much of the image you wish to RETAIN. The rest to be cropped away (for example 33% would by the integer 33)
    img = cv2.imread(img_path)
    print('in pre imageShow')
    height, width, channels = img.shape
    to_pixel = percentage / 100
    cv2.imshow('orig', img)
    cv2.waitKey(0)

    H_shear = int(width * to_pixel)
    #horizontal axis operations
    if segment == 'Left':
        left = img[:, :H_shear]
        lh, lw, _ = left.shape
        return (segment,left)

    if segment == 'Right':
        right = img[:, H_shear:]
        return (segment, right)

# this is vertical division

    v_shear =  int(height * to_pixel)

    if segment == 'Top':
        top = img[:v_shear, :]
        return (segment, top)

    if segment == 'Bottom':
        bottom = img[v_shear:, :]
        bh, bw, _ = bottom.shape
        print(f"Original height = {height} , width = {width} \n. Ratio: to_deci: {to_pixel} | {v_shear} - Percentage is: {percentage} , Cropped height : {bh} , crop width: {bw}")
        return (segment, bottom)


# images_dict = crawl_dir_for_files(os.path.abspath('specimen_images'))
images_dict = {}
output_dir = 'cropped_images'

def exe_cropping(specimen_images, cropped_dir):
    specimen_images_dir = specimen_images
    output_dir = cropped_dir
    images_dict = crawl_dir_for_files(os.path.abspath(specimen_images_dir))
    img_list = []

    for key in images_dict:
        print('IMAGES DICT ;', images_dict)
        img_path = images_dict[key]
        img_path = os.path.abspath(img_path)
        img_name = key
        print(f'img path:[{img_path}]')
        img = cv2.imread(img_path)

        shp = img.shape
        print(img_path, 'shape: ', shp)
        print('im path: ', img_path)
        cropped = crop_LRTB(img_path, 'Bottom', 25)
        print('LENGTH cropped = ', len(cropped) )
        crshp = cropped[1].shape
        print('cropped shape = ', crshp)

        cv2.imshow('crop', cropped[1])
        cv2.waitKey(0)

        cropped_path = os.path.abspath(output_dir)
        print('pre abs: --- ', output_dir)
        print('post abs: --- ', cropped_path)
        # os.chdir(output_dir)
        img_name = img_name.replace('.png', '')
        print('IMG_name minus suffix: ', img_name)
        print('writing to ? ', '{}/top cropped_{}.png'.format(cropped_path, img_name))
        cv2.imwrite('{}/top cropped_{}.png'.format(cropped_path, img_name), cropped[1])
        print('end of ', img_path)
    img_list = crawl_dir_for_files(cropped_path)
    return img_list




