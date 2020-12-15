# Course: CST 205
# Title: image_filter.py
# Abstract: This file creates a filtered version of an image. It has 3 filters: sepia, negative, and grayscale.
#           Images must be in PIL format for it to work.
# Author(s): Albert Salas (with filters adapted from Professor Biblarz' slides)
# 12/08/2020

from PIL import Image

class FilteredImage():
  def __init__(self, filter):
    # ensure that the filter name is always lowercase
    filter = filter.lower()
    # open image here
    image = Image.open("static/image.png")
    
    # This has allows us to call the appropiate function without
    # having to write a bunch of if statements
    filters = {
      "sepia": self.sepia,
      "negative": self.negative,
      "grayscale": self.grayscale,
    }

    if filter in filters:
      filtered_image = filters[filter](image)
      filtered_image.save("static/image.png")

  # Filters were adapted from Professor Biblarz' code
  def sepia(self, image):
    for x in range(image.width):
      for y in range(image.height):
        p = image.getpixel((x,y))
        if p[0] < 63:
          r,g,b = int(p[0] * 1.1), p[1], int(p[2] * 0.9)
        # tint midtones
        elif p[0] > 62 and p[0] < 192:
          r,g,b = int(p[0] * 1.15), p[1], int(p[2] * 0.85)
        # tint highlights
        else:
          r = int(p[0] * 1.08)
          if r > 255:
            r = 255
          g,b = p[1], int(p[2] * 0.5)

        image.putpixel((x,y), (r,g,b))
    return image

  def negative(self, image):
    for x in range(image.width):
      for y in range(image.height):
        p = image.getpixel((x,y))
        image.putpixel((x,y), tuple(map(lambda a : 255 - a, p)))
    return image

  def grayscale(self, image):
    for x in range(image.width):
      for y in range(image.height):
        p = image.getpixel((x,y))
        r = int(p[0] * 0.299)
        g = int(p[1] * 0.587)
        b = int(p[2] * 0.114)
        new_pixel = (r + g + b)
        image.putpixel((x,y), ((new_pixel,) * 3))
    return image
