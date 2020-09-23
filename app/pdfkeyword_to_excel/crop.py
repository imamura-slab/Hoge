import numpy as np
import cv2
import os


def crop(num):
    filename = "./input/input-" + str(num).zfill(6) + ".png"
    img      = cv2.imread(filename, 0)

    ID_img = img[419:472, 588:742]
    h, w   = ID_img.shape
    ratio  = 2
    ID_img = cv2.resize(ID_img, (w*ratio, h*ratio))
    threshold = 200
    _, ID_img = cv2.threshold(ID_img, threshold, 255, cv2.THRESH_BINARY)
    ID_filename = "./output/ID/" + str(num).zfill(6) + ".png"
    cv2.imwrite(ID_filename, ID_img)

    key_offset_u = 176
    key_offset_v = 543
    key_width    = 143
    key_height   = 35
    margin       = 4

    for i in range(5):
        for j in range(6):
            lt_u = key_offset_u + j*(key_width+margin)  + 2*(j//3)
            lt_v = key_offset_v + i*(key_height+margin)
            lt_v = lt_v if i<3 else lt_v-2
            rb_u = lt_u + key_width
            rb_v = lt_v + key_height

            ## crop
            key_img    = img[lt_v:rb_v, lt_u:rb_u]

            ## resize
            h, w       = key_img.shape
            ratio      = 3
            key_img    = cv2.resize(key_img, (w*ratio, h*ratio))

            ## binalize
            threshold  = 200
            _, key_img = cv2.threshold(key_img, threshold, 255, cv2.THRESH_BINARY)

            ## dilate and erode
            key_img = cv2.erode(key_img, (2,2), iterations=1)
            key_img = cv2.dilate(key_img, (5,5), iterations=1)
            
            index = j+i*6
            out_filename = "./output/keyword/" + str(num).zfill(6) + str(index).zfill(6) + ".png"
            cv2.imwrite(out_filename, key_img)

    

def main():
    for i in range(100):
        filename = "./input/input-" + str(i+1).zfill(6) + ".png"
        if os.path.exists(filename) is True:
            print('file', filename, 'exist!')
            crop(i+1)
        else:
            exit()

    
if __name__ == '__main__':
    main()

