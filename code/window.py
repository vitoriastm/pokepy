# Creation of the "Window" class
class Window:
    """
    Properties:
    __width = int,
    __height = int,
    __color = tuple
    """

    # Constructor method
    def __init__(self, width, height, color):
        self.__width = width
        self.__height = height
        self.__color = color

    @property
    # Returns the window size as a tuple (width, height)
    def returnWinSize(self):
        return (self.__width, self.__height)

    @property
    # Returns the color of the window (r, g, b)
    def returnColor(self):
        return self.__color