import numpy as np
import cv2
import copy
import math

#This is program will give you grayscale image as output
#You can give input as rbg image too

# for naming output window
names = {
    'a': "Arithmetic mean filter",
    'b': "Geometric mean filter",
    'c': "Median filter",
    'd': "Max filter",
    'e': "Min filter",
    'f': "Midpoint filter",
}

#reading original image and storing in image varibale
image = cv2.imread("imageOG.tif")
#replace imageOG.tif with your img url

#creating a grayscale of original image and storing in OGimage varibale (Original-Grayscale Image)
OGimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#making a deep copy of image and performing fliter on that deep copy
new_image = copy.deepcopy(OGimage)

#asking user to choose filter and masking size
filter_ = input("Choose a filter:\n"
                "'a' for Arithmetic mean filter\n"
                "'b' for Geometric mean filter\n"
                "'c' for Median filter\n"
                "'d' for Max filter\n"
                "'e' for Min filter\n"
                "'f' for Midpoint filter: ")
scale = int(input("Masking size: "))

# Arithmetic mean filter
if filter_ == 'a' or filter_ == 'A':
    print("Applying Arithmetic mean filter.......")
    for i in range(np.shape(OGimage)[0]):
        for j in range(np.shape(OGimage)[1]):
            #We will add intensity of all neighbours
            # and that pixel under operation to "pixels" list
            pixels = []
            # Iterating around all neighbours of that pixels
            for y in range(-math.floor(scale/2), math.floor(scale/2) + 1):
                for x in range(-math.floor(scale/2), math.floor(scale/2) + 1):
                    try:
                        pixels.append(OGimage[i + y, j + x])
                    except:
                        pass
            # Calculating avg of neighbour pixels
            avg = math.floor(sum(pixels) / len(pixels))
            # now replacing pixel's new intensity with 'avg'
            new_image[i, j] = avg

# Geometric mean filter
if filter_ == 'b' or filter_ == 'B':
    print("Applying Geometric mean filter......")
    for i in range(np.shape(OGimage)[0]):
        for j in range(np.shape(OGimage)[1]):
            pixels = []
            for y in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                for x in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                    try:
                        pixels.append(OGimage[i + y, j + x])
                    except:
                        pass
            product = math.prod(pixels)
            gp_avg = math.floor((product) ** (1 / len(pixels)))
            new_image[i, j] = gp_avg

# Median filter
if filter_ == 'c' or filter_ == 'C':
    print("Applying Median filter.......")
    for i in range(np.shape(OGimage)[0]):
        for j in range(np.shape(OGimage)[1]):
            pixels = []
            for y in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                for x in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                    try:
                        pixels.append(OGimage[i + y, j + x])
                    except:
                        pass
            pixels.sort()
            if len(pixels) % 2 == 0:
                i = int(len(pixels) / 2)
                median = math.floor((pixels[i - 1] + pixels[i + 1]) / 2)
            else:
                median = pixels[math.ceil(len(pixels) / 2)]
            new_image[i, j] = median

# Max filter
if filter_ == 'd' or filter_ == 'D':
    print("Applying Max filter.......")
    for i in range(np.shape(OGimage)[0]):
        for j in range(np.shape(OGimage)[1]):
            pixels = []
            for y in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                for x in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                    try:
                        pixels.append(OGimage[i + y, j + x])
                    except:
                        pass

            max_pixel = max(pixels)
            new_image[i, j] = max_pixel

# Min filter
if filter_ == 'e' or filter_ == 'E':
    print("Applying Min filter.......")
    for i in range(np.shape(OGimage)[0]):
        for j in range(np.shape(OGimage)[1]):
            pixels = []
            for y in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                for x in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                    try:
                        pixels.append(OGimage[i + y, j + x])
                    except:
                        pass

            min_pixel = min(pixels)
            new_image[i, j] = min_pixel
            
# Midpoint filter
if filter_ == 'f' or filter_ == 'F':
    print("Applying Midpoint filter.......")
    for i in range(np.shape(OGimage)[0]):
        for j in range(np.shape(OGimage)[1]):
            pixels = []
            for y in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                for x in range(-math.floor(scale / 2), math.floor(scale / 2) + 1):
                    try:
                        pixels.append(OGimage[i + y, j + x])
                    except:
                        pass

            mid_pixel = round((int(min(pixels)) + int(max(pixels))) / 2)

            new_image[i, j] = mid_pixel

cv2.imshow("Original", OGimage)
cv2.imshow(names[filter_.lower()],new_image)

cv2.waitKey(0)
