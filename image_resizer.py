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
        # dictinary to hold possible image manipulation
        sizes = {
            "enlarge": self.enlarge,
            "shrink": self.shrink,
            "rotate": self.rotate,
            "crop": self.crop,
            "flip": self.flip
        }
        # iterate through dictinart to see if passed option matches
        if size in sizes:
            resized_image = sizes[size](image)
            # saves modifies image
            resized_image.save("static/image.png")

    # enlarges an image by 1.5 times the original's size
    def enlarge(self, image):
        x = image.size[0]
        y = image.size[1]
        x = int(x * 1.5)
        y = int(y * 1.5)
        new_image = image.resize((x,y))
        return new_image

    # shrinks an image to half of the original's size
    def shrink(self, image):
        x = image.size[0]
        y = image.size[1]
        x = int(x * 0.5)
        y = int(y * 0.5)
        new_image = image.resize((x,y))
        return new_image

    # rotates an image 90 degrees
    def rotate(self, image):
        image_rot = image.rotate(90)
        return image_rot
    
    # crops in an an image 
    def crop(self, image):
        leftcrop = (image.size[0] - (image.size[0]/2))/2
        topcrop = (image.size[1] - (image.size[1]/2))/2
        rightcrop = (image.size[0] + (image.size[0]/2))/2
        botcrop = (image.size[1] + (image.size[1]/2))/2
        box = (leftcrop, topcrop, rightcrop, botcrop)
        cropped_image = image.crop(box)
        return cropped_image

    # flips an image by mirroring it
    def flip(self, image):
        image_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
        return image_flip
