"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    #Convert image as parameter into library code
    image = SimpleImage(filename)
    #Fetch width of an actual image
    width=image.width
    #Fetch height of an actual image
    height=image.height

    #Create a mirror image of an actual image for reflection
    #Define width similar to actual image  and height twice of actual image
    mirror=SimpleImage.blank(width*2 , height*2)

    #'For in range loop' for height
    for y in range(height):
        # 'For in range loop' for width
        for x in range(width):
            #Get " pixel of coordinates " of actual image at specific height and width
            pixel=image.get_pixel(x,y)
            #Set those coordinates and pixel to the mirror image of initial location
            mirror.set_pixel(x , y , pixel)

            """
            Set x coordinate as above and y coordinate 
            (after 2 times by height subtracting from coordinate (y+1) to decrease the height and print pixels)
            Then set pixel to that particular location 
            """
            #Bottom left
            mirror.set_pixel(x ,(height * 2) - (y+1) , pixel)
            #Top right
            mirror.set_pixel((width * 2) - (x+1) ,y , pixel)
            #Bottom right
            mirror.set_pixel((width * 2) - (x+1) , (height * 2) - (y+1) , pixel)
    return mirror


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
