import numpy as np
import math
import sys
import cv2

def intensity_4levels(base_matrices, n=2): # 0 1 2 3 (0 lightest, 3 darkest)
    matrices = []
    
    for matrix in base_matrices:
        matrices.append([row.copy() for row in matrix])

    if n >= 1:
        for matrix in matrices:
            matrix[1][2] = 1
    
    if n >= 2:
        for matrix in matrices:
            matrix[2][2] = 1

    if n >= 3:
        for matrix in matrices:
            matrix[2][1] = 1

    return matrices

def matrices4_to_8(matrices_4levels):
    matrices = []
    
    for matrix in matrices_4levels:
        matrices.append([row.copy() for row in matrix])

    # double matrices number
    length = len(matrices)
    for i in range(length):
        matrices.append([row.copy() for row in matrices[i]])
    
    for i in range(len(matrices)):
        if i < 4:
            matrices[i].insert(0, [0,1,0,1])
            matrices[i][1].append(0)
            matrices[i][2].append(1)
            matrices[i][3].append(0)
            matrices[i][3][2] = 1
        else:
            matrices[i].insert(0, [1,0,1,0])
            matrices[i][1].append(1)
            matrices[i][2].append(0)
            matrices[i][3].append(1)
    
    return matrices

def intensity_8levels(base_matrices, n=2): # 0 1 2 (0 lightest, 2 darkest)
    matrices = []
    
    for matrix in base_matrices:
        matrices.append([row.copy() for row in matrix])

    if n >= 1:
        for matrix in matrices:
            matrix[3][1] = 1
    
    if n >= 2:
        for matrix in matrices:
            matrix[2][2] = 1

    return matrices

base_greyscale_4levels = [[[1,0,1],
                           [1,0,0],
                           [0,0,0]], [[1,0,0],
                                      [1,1,0],
                                      [0,0,0]], [[0,1,1],
                                                 [0,0,0],
                                                 [1,0,0]], [[0,1,0],
                                                            [0,1,0],
                                                            [1,0,0]]]

greyscale_4levels = intensity_4levels(base_greyscale_4levels, 2)

base_greyscale_8levels = matrices4_to_8(base_greyscale_4levels)

greyscale_8levels = intensity_8levels(base_greyscale_8levels, 2)

def VC_conversion_diagonal(img):
    VC_img = np.zeros((img.shape[0]*2,img.shape[1]*2,4), np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_px_val = img[i][j][0]

            VC_img[i*2][j*2][3] = 255 - img_px_val
            
            VC_img[i*2][j*2 + 1][3] = img_px_val

            VC_img[i*2 + 1][j*2][3] = img_px_val

            VC_img[i*2 + 1][j*2 + 1][3] = 255 - img_px_val
    return VC_img

def VC_conversion_vertical(img):
    VC_img = np.zeros((img.shape[0]*2,img.shape[1]*2,4), np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_px_val = img[i][j][0]

            VC_img[i*2][j*2][3] = 255 - img_px_val
            
            VC_img[i*2][j*2 + 1][3] = img_px_val

            VC_img[i*2 + 1][j*2][3] = 255 - img_px_val

            VC_img[i*2 + 1][j*2 + 1][3] = img_px_val
    return VC_img

def VC_conversion_horizontal(img):
    VC_img = np.zeros((img.shape[0]*2,img.shape[1]*2,4), np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_px_val = img[i][j][0]

            VC_img[i*2][j*2][3] = 255 - img_px_val
            
            VC_img[i*2][j*2 + 1][3] = 255 - img_px_val

            VC_img[i*2 + 1][j*2][3] = img_px_val

            VC_img[i*2 + 1][j*2 + 1][3] = img_px_val
    return VC_img

def VC_conversion_greyscale_4levels(img):
    VC_img = np.zeros((img.shape[0]*3,img.shape[1]*3,4), np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            px_val = img[i][j][0]
            index = (int(px_val) + 1)//64 - 1
            for k in range(9):
                row = math.floor(k/3)
                column = k % 3
                VC_img[3*i+row][3*j+column][3] = greyscale_4levels[index][row][column]*255    #sets transparency to either 0 or 255 (all pixels are actually black)

    return VC_img

def VC_conversion_greyscale_8levels(img):
    VC_img = np.zeros((img.shape[0]*4,img.shape[1]*4,4), np.uint8)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            px_val = img[i][j][0]
            index = (int(px_val) + 1)//32 - 1
            for k in range(16):
                row = math.floor(k/4)
                column = k % 4
                VC_img[4*i+row][4*j+column][3] = greyscale_8levels[index][row][column]*255    #sets transparency to either 0 or 255 (all pixels are actually black)
    return VC_img

#filename = sys.argv[1]
#img = cv2.imread('../greyscale/outputs/' + filename)
#
#VC_img = VC_conversion_greyscale_8levels(img)
#
#cv2.imwrite('../greyscale/outputs/VC_' + filename, VC_img)
