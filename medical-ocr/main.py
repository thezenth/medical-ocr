import os

from PIL import Image
from pytesseract import *

dir = os.path.dirname(os.path.abspath(__file__))
print "=====DIR====="
print dir
image_file = dir + '/images/phototest.tif'

im = Image.open(image_file)
text = image_to_string(im)

print "=====output=======\n"
print text
