"""
File: codeinplace_filter.py
----------------
This program implements a rad image filter.
"""

from simpleimage import SimpleImage

DEFAULT_FILE = 'images/quad.jpg'

def code_in_place(filename):
    image=SimpleImage(filename)
    for pixel in image:
        pixel.red = pixel.red * 1.5
        pixel.green = pixel.green * 0.7
        pixel.blue = pixel.blue * 1.5
    return image


def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)
    # Show the image before the transform
    image.show()

    # code in place filter function
    c_i_p_f=code_in_place(filename)
    # code in place filter with show command
    c_i_p_f.show()
    

def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter for default): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()