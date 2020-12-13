# CST 205
# Shawn Deppe
# 12/12/2020
# Group Project - Team 28
# manipulates images using PIL

from PIL import Image

class resize_image():
    def __init__(self, size):
        # ensure that the filter name is always lowercase
        size = size.lower()
        image = Image.open("static/image.png")
        sizes = {
            "enlarge": self.enlarge,
            "shrink": self.shrink,
            "rotate": self.rotate,
            "crop": self.crop,
            "flip": self.flip
        }
        if size in sizes:
            resized_image = sizes[size](image)
            resized_image.save("static/image.png")

    def enlarge(self, image):
        x = image.size[0]
        y = image.size[1]
        x = x * 1.5
        y = y * 1.5
        new_image = image((x,y))
        return new_image

    def shrink(self, image):
        x = image.size[0]
        y = image.size[1]
        x = x * 0.5
        y = y * 0.5
        new_image = image((x, y))
        return new_image

    def rotate(self, image):
        image_rot = image.rotate(90)
        return image_rot
    
    def crop(self, image):
        box = (200, 300, 700, 600)
        cropped_image = image.crop(box)
        return cropped_image

    def flip(self, image):
        image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
        return image_flip
