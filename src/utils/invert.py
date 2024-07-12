import cv2
import numpy as np
import matplotlib.pyplot as plt

def invert(fileName):
  print(2)
  image = cv2.imread(fileName)
  image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  outputImage = cv2.bitwise_not(image)
  return outputImage
  # cv2.imwrite('{}_output.png'.format(fileName[:-4]), outputImage)
  # cv2.imwrite('{folderPath}/{inPath}_output.png'.format(folderPath="src/outputs", inPath=fileName[:-4]), outputImage)

