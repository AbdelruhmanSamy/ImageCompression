#!/bin/env python3
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dctn, idctn


def printGraph(PSNR_array):
    plt.plot(range(1, 5), PSNR_array, marker='o')
    plt.xlabel('m')
    plt.ylabel('PSNR')
    plt.title('m vs PSNR curve')
    plt.savefig('m_vs_PSNR.png')
    plt.show()


def getInput():
    imageName = input("Enter the name of the image file: ")
    if imageName == "":
        imageName = "image.png"
    image = cv2.imread(imageName)
    for color in range(3):
        coloredImage = np.zeros_like(image)
        coloredImage[:, :, color] = image[:, :, color]
        cv2.imwrite(f"color{color}.png", coloredImage)
    return image


def main(image, length, width, PSNR_array, m):
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

    PSNR_array.append(cv2.PSNR(image, decompressedImage))
    cv2.imwrite(f"compressed{m}.png", compressedImage)
    cv2.imwrite(f"decompressed{m}.png", decompressedImage)


if __name__ == "__main__":
    PSNR_array = []
    image = getInput()
    length = image.shape[0]
    width = image.shape[1]
    for m in range(1, 5):
        main(image, length, width, PSNR_array, m)
    printGraph(PSNR_array)
