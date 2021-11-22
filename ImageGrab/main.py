from PIL import ImageGrab
import datetime
import os

img = ImageGrab.grab()
my_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
file_name =  "my_" + my_time + ".jpg"
img.save(file_name, "JPEG")