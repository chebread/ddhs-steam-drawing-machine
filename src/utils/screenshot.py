import time
import pyscreenshot as ImageGrab
import cv2

def screenshot():
  # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
  current_time = time.strftime("%Y%m%d_%H%M%S")
  img = ImageGrab.grab()
  fileName = "src/screenshots/{}.png".format(current_time)
  img.save(fileName)  # image_20200601_102030 .png
  return fileName