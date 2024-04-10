#!/usr/bin/python3
""" task 1"""


class Rectangle:
    """a class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """" returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' calc area'''
        return self.__width * self.__height

    def perimeter(self):
        '''calc perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''print rect'''
        if self.__width == 0 or self.__height == 0:
            return ""
        rectstr = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectstr.append(str(self.print_symbol))
            if i < self.__height - 1:
                rectstr.append('\n')
        return ''.join(rectstr)

    def __repr__(self):
        ''' return str repr'''
        rectstr = "Rectangle"+"("+str(self.__width)+", "+str(self.__height)+")"
        return rectstr

    def __del__(self):
        '''deletes'''
        del self
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' returns the bigger rect'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 > area_2 or area_1 == area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''returns a new Rectangle instance with width == height == size'''
        return cls(size, size)