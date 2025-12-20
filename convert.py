from PIL import Image

img = Image.open('test.bmp')
img.save('./assets/final.png', compress_level=9)