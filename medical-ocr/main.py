import os

from debug import *

from PIL import Image
from pytesseract import *

dir = os.path.dirname(os.path.abspath(__file__))
dbg(dir, clr='blue', ident="dir")
image_file = dir + '/images/phototest.tif'

im = Image.open(image_file)
text = image_to_string(im)

dbg(text, clr='green', ident="ocr-output")
