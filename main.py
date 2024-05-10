#!/bin/env python3
import cv2
import numpy as np
from scipy.fft import dctn, idctn


def getInput():
    """Get the input image and split it into its RGB channels."""
    imageName = input("Enter the name of the image file: ")
    m = int(input("Enter value of m: "))

    image = cv2.imread(imageName)

    return image, m


def main():
    """Execute the program."""
    image, m = getInput()
    length = image.shape[0]
    width = image.shape[1]

    # Initialize the compressed and decompressed images
    compressedImage = np.zeros_like(image)
    decompressedImage = np.zeros_like(image)

    # Compress the image
    for color in range(3):
        channel = image[:, :, color]
        for i in range(0, length, 8):
            for j in range(0, width, 8):
                block = dctn(channel[i:i+8, j:j+8])
                block[m:, :] = 0
                block[:, m:] = 0
                compressedImage[i:i+8, j:j+8, color] = block
                decompressedBlock = idctn(block)
                np.clip(decompressedBlock, 0, 255, out=decompressedBlock)
                decompressedImage[i:i+8, j:j+8, color] = decompressedBlock

    cv2.imwrite("compressed.png", compressedImage)
    cv2.imwrite("decompressed.png", decompressedImage)


if __name__ == "__main__":
    main()
