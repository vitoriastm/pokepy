import pygame

# Creation of "Imgbutton" class

class ImgButton:
    """
    Properties:
    position,
    img_file_name,
    image,
    """

    def __init__(self, x, y, img_file_name, function):
        self.__x = x
        self.__y = y
        self.__img_file_name = img_file_name
        self.__image = pygame.image.load(self.__img_file_name)
        self.__function = function

    @property
    def function(self):
        return self.__function
        
    @property
    def image(self):
        return self.__image
        
    @property
    def size(self):
        self.__size = self.__image.get_rect().size
        return self.__size

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def img_file_name(self):
        return self.__img_file_name

    @function.setter
    def set_function(self, function):
        self.__function = function
    
    @x.setter
    def set_x(self, new_x):
        self.__x = new_x

    @y.setter
    def set_y(self, new_y):
        self.__y = new_y

    def __contains__(self, point):
        x0, y0 = self.__x, self.__y
        dx, dy = self.size
        px, py = point

        contains_x = x0 <= px <= x0 + dx
        contains_y = y0 <= py <= y0 + dy

        return contains_x and contains_y


# Creation of "PokemonButton" class

class PokemonButton:
    """
    Properties:
    position,
    img_file_name,
    image,
    """

    def __init__(self, x, y, img_file_name, pokemon):
        self.__x = x
        self.__y = y
        self.__img_file_name = img_file_name
        self.__image = pygame.image.load(self.__img_file_name)
        self.__pokemon = pokemon

    @property
    def function(self):
        return self.pokemon.name

    @property
    def pokemon(self):
        return self.__pokemon
        
    @property
    def image(self):
        return self.__image
        
    @property
    def size(self):
        self.__size = self.__image.get_rect().size
        return self.__size

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def img_file_name(self):
        return self.__img_file_name

    @x.setter
    def set_x(self, new_x):
        self.__x = new_x

    @y.setter
    def set_y(self, new_y):
        self.__y = new_y

    def __contains__(self, point):
        x0, y0 = self.__x, self.__y
        dx, dy = self.size
        px, py = point

        contains_x = x0 <= px <= x0 + dx
        contains_y = y0 <= py <= y0 + dy

        return contains_x and contains_y