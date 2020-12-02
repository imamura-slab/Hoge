import numpy as np
import cv2

HEIGHT = 240
WIDTH  = 320

path_r = "output_data/data_r.hex"
path_g = "output_data/data_g.hex"
path_b = "output_data/data_b.hex"


def main():
    with open(path_r) as f:
        data_r = [int(s.strip(),16) for s in f.readlines()]
    with open(path_g) as f:
        data_g = [int(s.strip(),16) for s in f.readlines()]
    with open(path_b) as f:
        data_b = [int(s.strip(),16) for s in f.readlines()]


    frames = int(len(data_r) / (HEIGHT*WIDTH))
    print(frames, "frames")
    img = np.zeros((HEIGHT, WIDTH, 3))
    print(img.shape)
    for frame in range(frames):
        for i in range(HEIGHT):
            for j in range(WIDTH):
                index = frame*HEIGHT*WIDTH + i*WIDTH + j
                img[i,j,2] = data_r[index]
                img[i,j,1] = data_g[index]
                img[i,j,0] = data_b[index]
        cv2.imwrite("output_img/" + str(frame).zfill(3) + ".png", img)
            
    


if __name__ == '__main__':
    main()
