#!/bin/python3
import cv2
import numpy as np

def DCT(block , m):
    dctImg = cv2.dct(np.float32(block))
    compDctImg = dctImg[:m][:m]
    return compDctImg

def iDCT(retainedCoeff ,  m):
    pad_size = 8 - m
    padded_array = np.pad(retainedCoeff, ((0, pad_size), (0, pad_size)), 'constant')
    imatrix = cv2.idct(np.float32(padded_array))
    return imatrix
    
if __name__ == "__main__":
    m = 2
    imageTest = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    freqarr = DCT(imageTest, m)
    
    for i in range(m):
        for j in  range(m):
            print(f"{freqarr[i][j]} ", end="")
        print()        
    
    ifreqarr = iDCT(freqarr , m)

    for i in range(8-m):
        for j in  range(8-m):
            print(f"{ifreqarr[i][j]} ", end="")
        print() 
