# Importing Pygame and Random libraries
import pygame
import random

# Creation of the "Pokemon" class
class Pokemon:
    """
    Properties:
    name = str,
    n = int,
    lvl = int,
    types = [],
    gender = str,
    attacks = [attack],
    hp_max = int / float,
    damage = int / float,
    front_img,
    back_img,
    """
    def __init__(self, name, n, Type, level, gender, base_list, moves):
        self.__name = name
        self.__n = n
        self.__Type = Type
        self.__level = level
        self.__gender = gender
        self.__damage = 0
        self.__currently_attack = 0
        self.__base_list = base_list
        self.__base_stats = {
            "base_hp" : self.__base_list[0],
            "base_attack" : self.__base_list[1],
            "base_defense" : self.__base_list[2],
            "base_spAttack" : self.__base_list[3],
            "base_spDefense" : self.__base_list[4],
            "base_speed" : self.__base_list[5]
        }
        self.__moves = moves
        self.__iv = random.randint(0,32)
        self.__ev = 500
        self.__hp = int((((2 * self.__base_stats["base_hp"] + self.__iv + (self.__ev / 4)) * self.__level) / 100) + self.__level + 10)
        self.__attack = int(((((2 * self.__base_stats["base_attack"] * self.__iv * (self.__ev / 4)) * self.__level) / 100) + 5) * 1)
        self.__defense = int(((((2 * self.__base_stats["base_defense"] * self.__iv * (self.__ev / 4)) * self.__level) / 100) + 5) * 1)
        self.__spAttack = int(((((2 * self.__base_stats["base_spAttack"] * self.__iv * (self.__ev / 4)) * self.__level) / 100) + 5) * 1)
        self.__spDefense = int(((((2 * self.__base_stats["base_spDefense"] * self.__iv * (self.__ev / 4)) * self.__level) / 100) + 5) * 1)
        self.__speed = int(((((2 * self.__base_stats["base_speed"] * self.__iv * (self.__ev / 4)) * self.__level) / 100) + 5) * 1)
        self.__state = "okay"

    @property
    def name(self):
        return self.__name

    @property
    def n(self):
        return self.__n

    @property
    def Type(self):
        return self.__Type

    @property
    def level(self):
        return self.__level

    @property
    def gender(self):
        return self.__gender
    
    @property
    def damage(self):
        return self.__damage

    @property
    def iv(self):
        return self.__iv

    @property
    def hp(self):
        return self.__hp

    @property
    def attack(self):
        return self.__attack

    @property
    def defense(self):
        return self.__defense

    @property
    def spAttack(self):
        return self.__spAttack

    @property
    def spDefense(self):
        return self.__spDefense

    @property
    def speed(self):
        return self.__speed

    @property
    def moves(self):
        return self.__moves
    
    def set_img(self, front_img, back_img, colored_imgf, colored_imgb):
        self.__front_img = pygame.image.load(front_img)
        self.__back_img = pygame.image.load(back_img)
        self.__colored_imgf = pygame.image.load(colored_imgf)
        self.__colored_imgb = pygame.image.load(colored_imgb)

    @property
    def front_img(self):
        return self.__front_img

    @property
    def back_img(self):
        return self.__back_img

    @property
    def colored_imgf(self):
        return self.__colored_imgf

    @property
    def colored_imgb(self):
        return self.__colored_imgb

    @damage.setter
    def damage(self, acdamage):
        self.__damage += acdamage

    def set_currently_attack(self, index):
        self.__currently_attack = self.__moves[index]

    @property
    def currently_attack(self):
        return self.__currently_attack

    def set_state(self, new_state):
        self.__state = new_state

    @property
    def state(self):
        return self.__state