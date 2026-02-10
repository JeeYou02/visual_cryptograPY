import numpy as np
import sys
import cv2

# ====================== 4 LEVELS =======================

def encrypt_4levels(n,m):   #n,m are gray levels in {1,2,3,4}
    assert n >= 1 and n <= 4 and m >= 1 and m <= 4, "Bad values m = " + str(m) + ", n = " + str(n)

    if(n == 4):
        return m
    if(m == 4):
        return n
    if(n == m):
        return 4
    if(n == 3):
        return abs(m - 2) + 1
    if(n == 2 and m == 1):
        return 3
    return encrypt_4levels(m,n)

def encrypt_image_4levels(img, key):
    cypher = np.zeros((key.shape[0], key.shape[1],3), np.uint8)

    for i in range(key.shape[0]):
        for j in range(key.shape[1]):
            key_val = key[i][j][0]
            img_val = img[i][j][0]

            cypher[i][j] = encrypt_4levels((int(key_val)+1)//64, (int(img_val)+1)//64)*64 - 1
    
    return cypher

# ===================== 8 LEVELS ======================

def domain_conversion_to_4L(n):
    if n == 4 or n == 8:
        return 4
    else:
        return n % 4


def encrypt_8levels(n,m): #n,m are gray levels in {1,2,3,4,5,6,7,8}
    assert n >= 1 and n <= 8 and m >= 1 and m <= 8, "Bad values m = " + str(m) + ", n = " + str(n)

    nc = domain_conversion_to_4L(n)
    mc = domain_conversion_to_4L(m)

    if (n <= 4 and m <= 4) or (n >= 5 and m >= 5):
        return encrypt_4levels(nc,mc) + 4

    return encrypt_4levels(nc,mc)

def encrypt_image_8levels(img, key):
    cypher = np.zeros((key.shape[0], key.shape[1],3), np.uint8)

    for i in range(key.shape[0]):
        for j in range(key.shape[1]):
            key_val = key[i][j][0]
            img_val = img[i][j][0]

            cypher[i][j] = encrypt_8levels((int(key_val)+1)//32, (int(img_val)+1)//32)*32 - 1
    
    return cypher

##img_path = sys.argv[1]
##key_path = sys.argv[2]
#key = cv2.imread('outputs/key.png')
#img = cv2.imread('outputs/quantized_image.png')
#
#cypher = encrypt_4levels(img, key)
#
#cv2.imwrite('outputs/cypher.png', cypher)
