#!/usr/bin/python3
"""
A Module for modeling Square obj
"""


class square():
    """ A class Square
    """

    def __init__(self, width, height):
        """
        initialize
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String format of square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """
    deriver code
    """
    s = square(width=9, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
