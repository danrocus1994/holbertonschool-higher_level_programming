#!/usr/bin/python3
"""rectangle module"""


from models.base import Base


class Rectangle(Base):
    """rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    @property
    def width(self):
        """property"""
        return self.__width

    @width.setter
    def width(self, value):
        """property"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("with must be > 0")
        self.__width = value

    @property
    def height(self):
        """property"""
        return self.__height

    @height.setter
    def height(self, value):
        """property"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """property"""
        return self.__x

    @x.setter
    def x(self, value):
        """property"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """property"""
        return self.__y

    @y.setter
    def y(self, value):
        """property"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the are"""
        return self.__width * self.__height

    def display(self):
        """print rectangle representation with #"""
        for y in range(self.__y):
            print()
        for h in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """return string representation of rectangle"""
        return "[{}] ({}) {}/{} - {}/{}"\
            .format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)


    def update(self, *args, **kwargs):
        """updating attributes function"""
        attrs = ["id", "width", "height", "x", "y"]
        argus = list(args)
        if len(argus) > 0:
            for i, arg in enumerate(argus):
                setattr(self, attrs[i], arg)
        else:
            for kwarg in kwargs.items():
                setattr(self, kwarg[0], kwarg[1])

    def to_dictionary(self):
        dic = self.__dict__
        attrs = ["id", "width", "height", "x", "y"]
        ret = {x: getattr(self, x) for x in attrs }
        return ret
