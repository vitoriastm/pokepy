# Player class creation

class Player:
    '''
    Properties:
    name = str,
    pokemon_list = [Pokemon],
    backpack = [Item],
    sprites = [
        menu,
        choosing_menu,
        in_battle
    ]
    '''
    def __init__(self, name, pokemon_list, backpack, sprites):
        self.__name = name
        self.__pokemon_list = pokemon_list
        self.__backpack = backpack
        self.__sprites = sprites
        self.__in_battle = 0

    @property
    def name(self):
        return self.__name

    @property
    def pokemon_list(self):
        return self.__pokemon_list

    @property
    def backpack(self):
        return self.__backpack

    @property
    def sprites(self, n):
        return self.__sprites[n]
    
    @property
    def poke_num(self):
        i = 0
        for pokemon in self.__pokemon_list:
            if pokemon != "":
                i += 1
        return i

    @property
    def in_battle(self):
        return self.__pokemon_list[self.__in_battle]

    @in_battle.setter
    def in_battle(self, index):
        self.__in_battle = index

    def set_pokemon(self, pokemon, n):
        self.__pokemon_list[n] = pokemon
    
    