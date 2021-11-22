from PIL import ImageGrab
import datetime
import os

img = ImageGrab.grab()
img.save('screen.png', 'PNG')