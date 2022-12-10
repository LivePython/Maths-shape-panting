import numpy as np
from pil import Image


class Canvas:
    """
    The canvas the object on which the shapes are drawn
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        # Create numpy array of zeros
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        """
        Convert the current array into image
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
