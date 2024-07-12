import time
import pyscreenshot as ImageGrab

def screenshot():
  print(1)
  # 2020년 6월 1일 10시 20분 30초 -> _20200601_102030
  current_time = time.strftime("_%Y%m%d_%H%M%S")
  img = ImageGrab.grab()
  img.save("src/screenshots/{}.png".format(current_time))  # image_20200601_102030 .png