#!/bin/env python3
import cv2


def DCT(block, m):
    return


def getInput():
    """Get the input image and split it into its RGB channels."""
    imageName = input("Enter the name of the image file: ")
    m = input("Enter value of m: ")

    image = cv2.imread(imageName)
    blueChannel, greenChannel, redChannel = cv2.split(image)

    return blueChannel, greenChannel, redChannel, m


def main():
    """Execute the program."""
    blueChannel, greenChannel, redChannel, m = getInput()

    for i in range(0, len(blueChannel), 8):
        for j in range(0, len(blueChannel[0]), 8):
            DCT(blueChannel[i : i + 8, j : j + 8], m)

    for i in range(0, len(greenChannel), 8):
        for j in range(0, len(greenChannel[0]), 8):
            DCT(greenChannel[i : i + 8, j : j + 8], m)

    for i in range(0, len(redChannel), 8):
        for j in range(0, len(redChannel[0]), 8):
            DCT(redChannel[i : i + 8, j : j + 8], m)
