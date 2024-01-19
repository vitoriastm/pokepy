# Poképy: Battle Simulator (main) #

#________________________________________________________________________________________________________#
# 1. Basic Functions:

# Importing libraries and modules
import pygame
import random
import sys
import time
import numpy as np
from window import Window
from button import ImgButton
from button import PokemonButton
from move import Move
from pokemon import Pokemon
from player import Player

# Creation of the clock object
clock = pygame.time.Clock()

# Boolean used on the main loop
running = True

# Setting cursor value as 0:
cursor = 0

# Initiating pygame functions
pygame.init()
pygame.mixer.init()
pygame.font.init()

#________________________________________________________________________________________________________#
# 2. Setting display screen:

# Setting window's name
pygame.display.set_caption("Poképy")

# Loading and setting window's icon
programIcon = pygame.image.load('main/icon.png')
pygame.display.set_icon(programIcon)

# Creation of the "w" object of "Window class", with 800px (height) and 600px (width)
w = Window(800, 600, (0,0,0))

# Initiating the window
win = pygame.display.set_mode(w.returnWinSize)

# Setting the black color for the window
win.fill(w.returnColor)

#________________________________________________________________________________________________________#
# 3. Visual functions and sound effects:

# Function that returns the image height
def get_height(image):
    size = image.get_rect().size
    return size[1]
    
# Function that returns the image width
def get_width(image):
    size = image.get_rect().size
    return size[0]

# Print button function
def print_button(screen, button, highlighted = False):

    # Setting position and image
    position = button.x, button.y
    image = button.image

    # If highlighted = True:
    if highlighted:
        # Print the button image
        screen.blit(image, position)
        # Print the pointer image
        screen.blit(pointer, ((position[0] - 21), (position[1] - 3)))

    # If highlighted = False:
    else:
        # Just print the button image
        screen.blit(image, position)

# Text function
def text(surface, text, font, x, y, color):
    text = font.render(text, True, color)
    textRect = text.get_rect()
    textRect.topleft = (x , y)
    win.blit(text, textRect)

# Loading pointer image
pointer = pygame.image.load('main/pointer.png')

# Loading menu sound effect:
plim = pygame.mixer.Sound('music and sound/cursor_sound_effect.wav')

#________________________________________________________________________________________________________#
# 4. Setting players:

# Loading players sprites
player1_sprites = {
    "menu" : (pygame.image.load('menu/P1.png'), (37,117)),
    "title" : (pygame.image.load('menu/player1_title.png'), (75, 73)),
    "choose" : (pygame.image.load('choose_interface/P1choose.png'), (29, 123)),
    "in_battle" : (pygame.image.load('battle/player1_animation/0.png'))
}

player2_sprites = {
    "menu" : (pygame.image.load('menu/P2.png'), (498, 117)),
    "title" : (pygame.image.load('menu/player2_title.png'), (529, 73)),
    "choose" : (pygame.image.load('choose_interface/P2choose.png'), (29, 123)),
    "in_battle" : (pygame.image.load("battle/p2_char.png"))
}

# Creating player1 and player2 object
player1 = Player("PLAYER 1", ["", "", "", ""], [], player1_sprites)
player2 = Player("PLAYER 2", ["", "", "", ""], [], player2_sprites)

#________________________________________________________________________________________________________#
# Setting Pokémon attacks:

tackle = Move("Tackle", "Normal", 40, 35, 100)
growl = Move("Growl", "Normal", 0, 40, 100)
solar_beam = Move("Solar Beam", "Grass", 120, 10, 100)
razor_leaf = Move("Razor Leaf", "Grass", 55, 25, 95)
dragon_rage = Move("Dragon Rage", "Dragon", 0, 10, 100)
flamethrower = Move("Flamethrower", "Fire", 90, 15, 100)
slash = Move("Slash", "Normal", 70, 20, 100)
hydro_pump = Move("Hydro Pump", "Water", 110, 5, 80)
rain_dance = Move("Rain Dance", "Water", 0, 5, 0)
bite = Move("Bite", "Dark", 60, 25, 100)
thunder_wave = Move("Thunder Wave", "Electric", 0, 20, 90)
slam = Move("Slam", "Normal", 80, 20, 75)
thunderbolt = Move("Thunderbolt", "Electric", 90, 15, 100)
twister = Move("Twister", "Dragon", 40, 20, 100)

# Grouping them on a list
pokemon_moves =[
    tackle,
    growl,
    solar_beam,
    razor_leaf,
    dragon_rage,
    flamethrower,
    slash,
    hydro_pump,
    rain_dance,
    bite,
    thunder_wave,
    slam,
    thunderbolt,
    twister
]
size = pointer.get_rect().size

#________________________________________________________________________________________________________#
# 5. Setting Pokémon:

# Bulbasaur
bulbasaur = Pokemon("Bulbasaur", 1, ["grass", "poison"], 50, "F", [45, 49, 49, 65, 65, 45], [tackle, growl, solar_beam, razor_leaf])

# Charmander
charmander = Pokemon("Charmander", 4, ["fire"], 50, "M", [39, 52, 43, 60, 50, 65], [growl, dragon_rage, flamethrower, slash])

# Charizard
charizard = Pokemon("Charizard", 6, ["fire", "flying"], 50, "M", [78, 84, 78, 109, 85, 100], [growl, dragon_rage, flamethrower, slash])

# Squirtle
squirtle = Pokemon ("Squirtle", 7, ["water"], 50, "M", [44, 48, 65, 50, 64, 43], [tackle, hydro_pump, rain_dance, bite])

# Blastoise
blastoise = Pokemon("Blastoise", 9, ["water"], 50, "F", [79, 83, 100, 85, 105, 78], [tackle, hydro_pump, rain_dance, bite])

# Pikachu
pikachu = Pokemon("Pikachu", 25, ["electric"], 50, "F", [35, 55, 30, 50, 40, 90], [growl, thunder_wave, slam, thunderbolt])

# Gyarados
gyarados = Pokemon("Gyarados", 130, ["water", "flying"], 50, "M", [95, 125, 79, 60, 100, 81], [dragon_rage, hydro_pump, rain_dance, bite])

# Dratini
dratini = Pokemon("Dratini", 148, ["dragon"], 50, "F", [41, 64, 45, 50, 50, 50], [thunder_wave, slam, dragon_rage, twister])


# Setting selectable Pokémon list:
selectable_pokemon = [
    bulbasaur, 
    charmander, 
    charizard, 
    squirtle, 
    blastoise, 
    pikachu,
    gyarados, 
    dratini 
    ]

# Loading pokémon images (front and back)
for pokemon in selectable_pokemon:
    # Setting file names
    front_img = f'pokemon/front/{pokemon.n}.png'
    back_img = f'pokemon/back/{pokemon.n}.png'
    colored_imgf = f'pokemon/pink/front/{pokemon.n}.png'
    colored_imgb = f'pokemon/pink/back/{pokemon.n}.png'
    # Setting images
    pokemon.set_img(front_img, back_img, colored_imgf, colored_imgb)

#________________________________________________________________________________________________________#
# 6. Setting game opening:

# Loading opening music
opening_music = 'music and sound/opening_music.wav'

# Loading opening images
opening1 = pygame.image.load("opening/opening1.png")
opening2 = pygame.image.load("opening/opening2.jpg")
press_start = pygame.image.load("opening/pressStart.png")
charmander1 = pygame.image.load("opening/charmander1.png")
charmander2 = pygame.image.load("opening/charmander2.png")
flash = pygame.image.load("opening/flash.png")
pokepy1 = pygame.image.load("opening/pokepy.png")
battle_simulator = pygame.image.load("opening/battle_simulator.png")

# setting blink variable used on press start button animation
blink = 0

# setting initial flash y coordinate used on opening animation
flash_y = 600

# setting charmander b/w image alpha
charmander_alph = 0

#________________________________________________________________________________________________________#
# 7. Setting main menu:

allset = pygame.image.load("menu/all_set.png")

# Loading menu background
background = (pygame.image.load('main/background.jpg'), (0,0))

# Loading poképy title image
pokepy = (pygame.image.load('main/pokepy.png')), (280,10)

# Loading menu background music
menu_music = 'music and sound/ViridianCity.mp3'

# Grouping menu images on a list
menu_images = [
    background,
    pokepy,
    player1_sprites["title"], 
    player2_sprites["title"], 
    player1_sprites["menu"], 
    player2_sprites["menu"]
    ]

# Setting the first button:
position1 = (88, 418)
choose_button1 = ImgButton(position1[0], position1[1], 'menu/choose.png', 'chooseP1')

# Setting the second button:
position2 = (546, 418)
choose_button2 = ImgButton(position2[0], position2[1], 'menu/choose.png', 'chooseP2')

# Setting the third button:
position3 = (46, 460)
randomize_button1 = ImgButton(position3[0], position3[1], 'menu/randomize.png', 'randomizeP1')

# Setting the fourth button:
position4 = (504, 459)
randomize_button2 = ImgButton(position4[0], position4[1], 'menu/randomize.png', 'randomizeP2')

# Setting the fifth button:
position5 = (174, 507)
start_battle = ImgButton(position5[0], position5[1], 'menu/start_battle.png', 'startBattle')
    
# Creation of menu buttons list:
menu_buttons = [
    choose_button1,
    choose_button2,
    randomize_button1,
    randomize_button2,
    start_battle
]

# Creation of menu buttons positions list:
menu_bpositions = [
    position1,
    position2,
    position3,
    position4,
    position5
]

# setting all_set variable, that determinates if battle can start
all_set = False

#________________________________________________________________________________________________________#
# 8. Setting choose menu:

# Loading fonts
font_size1 = pygame.font.Font('fonts/fontePygame.ttf', 20)
font_size2 = pygame.font.Font('fonts/fontePygame.ttf', 29)
font_size3 = pygame.font.Font('fonts/fontePygame.ttf', 24)

# Loading images:

# Background:
background = (pygame.image.load('main/background.jpg'), (0,0))

# Pokémon list frame:
frame = (pygame.image.load('choose_interface/frame.png'), (234, 63))

# Choosing menu pokeballs:
pokeball1 = (pygame.image.load('choose_interface/pokeballchoose.png'), (12, 376))
pokeball2 = (pygame.image.load('choose_interface/pokeballchoose.png'), (12, 412))
pokeball3 = (pygame.image.load('choose_interface/pokeballchoose.png'), (12, 448))
pokeball4 = (pygame.image.load('choose_interface/pokeballchoose.png'), (12, 484))

# Grouping them on a list:
choose_screen = [
    background,
    frame,
    pokeball1,
    pokeball2,
    pokeball3,
    pokeball4
]

# Setting selectable pokémon buttons

bulbasaur_button = PokemonButton(0, 0, "pokemon/name/1.png", bulbasaur)
charmander_button = PokemonButton(0, 0, "pokemon/name/4.png", charmander)
charizard_button = PokemonButton(0, 0, "pokemon/name/6.png", charizard)
squirtle_button = PokemonButton(0, 0, "pokemon/name/7.png", squirtle)
blastoise_button = PokemonButton(0, 0, "pokemon/name/9.png", blastoise)
pikachu_button = PokemonButton(0, 0, "pokemon/name/25.png", pikachu)
gyarados_button = PokemonButton(0, 0, "pokemon/name/130.png", gyarados)
dratini_button = PokemonButton(0, 0, "pokemon/name/148.png", dratini)

# Setting variables that will receive buttons positions values:
cposition1 = [0, 0]
cposition2 = [0, 0]
cposition3 = [0, 0]
cposition4 = [0, 0]
cposition5 = [0, 0]
cposition6 = [0, 0]
cposition7 = [0, 0]
cposition8 = [0, 0]
cposition9 = [43, 563]

# Setting back button
back = ImgButton(cposition9[0], cposition9[1], 'choose_interface/back.png', 'back')

# Variable used to change pokémon tag position on list
new_y = 112
# Original tag position
xc = 285
yc = 112
# Variables used when a pokémon is chosen
n1 = 0
n2 = 0

# Creation of a list that contains choose screen buttons:
choose_buttons = [
    bulbasaur_button,
    charmander_button,
    charizard_button,
    squirtle_button,
    blastoise_button,
    pikachu_button,
    gyarados_button,
    dratini_button,
    back
]

# Creation of a list that contains choose screen buttons positions:
choose_positions = [
    cposition1,
    cposition2,
    cposition3,
    cposition4,
    cposition5,
    cposition6,
    cposition7,
    cposition8,
    cposition9
]

# Function that prints stats from the current selected Pokémon at choosing list
def print_stats(button):

    poke = button.pokemon

    # setting position
    x = 618
    y = 62
    
    # setting image
    width = get_width(poke.front_img) * 5 // 2
    height = get_height(poke.front_img) * 5 // 2 
    bigger_img = pygame.transform.scale(poke.front_img, (width, height))
    win.blit(bigger_img, (x,y))

    # setting name
    title = button.image
    w = get_width(title)
    w = (w * 150) // w
    h = get_height(title)
    h = (h * 12) // h
    smaller_name = pygame.transform.scale(title, (w, h))
    win.blit(smaller_name, (x - 10, (y + height + 10)))

    # setting types
    types = poke.Type
    contador = 0

    for Type in types:
        type_label = pygame.image.load(f"pokemon/types/{Type}.png")
        wt = get_width(type_label)
        wt = (wt * 85) // wt
        ht = get_height(type_label)
        ht = (ht * 32) // ht
        type_label = pygame.transform.scale(type_label, (wt, ht))

        pos = ((x + 30) , (y + ht + 170))

        if contador == 0 and len(types) == 1:
            win.blit(type_label, pos)

        if contador == 0 and len(types) == 2:
            pos = ((x - 10) , (y + ht + 170))
            win.blit(type_label, pos)

        elif contador == 1 and len(types) == 2:
            pos = ((x + 85) , (y + ht + 170))
            win.blit(type_label, pos)

        contador += 1

    # setting hp

    hp = f"HP: {str(poke.hp)}"
    hp = font_size1.render(hp, True, (255, 255, 255))
    hpRect = hp.get_rect()

    hpRect.midtop = ((get_width(bigger_img) // 2) + x, (y + 310))

    win.blit(hp, hpRect)

    # setting attack
    '''
    attack = f"Attack: {str(poke.attack)}"
    attack = font_size1.render(attack, True, (255, 255, 255))
    attackRect = attack.get_rect()

    attackRect.midtop = ((get_width(bigger_img) // 2) + x, (y + 350))

    win.blit(attack, attackRect)
    '''

    # setting defense
    '''
    defense = poke.defense
    text(win, f"Defense: {defense}", font_size1, x, y, (255, 255, 255))
    '''

    # setting gender
    gender = poke.gender
    gender_symbol = pygame.transform.scale((pygame.image.load(f"choose_interface/{gender}.png")), (15, 24))
    win.blit(gender_symbol, (x + w + 5, (y + height + 5)))

    # setting lvl
    level = f"LEVEL: {str(poke.level)}"
    level = font_size1.render(level, True, (255, 255, 255))
    levelRect = level.get_rect()

    levelRect.midtop = ((get_width(bigger_img) // 2) + x, (y + 280))

    win.blit(level, levelRect)

    # setting number
    
    number = str(poke.n)
    c = 0

    for num in number:
        c += 1

    num = num

    if c == 1:
        number = "00" + number

    elif c == 2:
        number = "0" + number
        
    text(win, f"#{number}", font_size1, (get_width(poke.front_img) // 2) + x, y + 250, (255, 255, 255))

    '''
    number = font_size1.render((f"N: {poke.n}"), True, (255, 255, 255))
    num_rect = number.get_rect()
    num_rect.topleft = ((x + 20), (y + 200))
    win.blit(number, num_rect)
    '''

#________________________________________________________________________________________________________#
# 9. Setting battle interface:


# Loading battle music
battle_music = 'music and sound/battle_music.wav'

# Loading fonts
font2 = pygame.font.Font('fonts/RetroGaming.ttf', 25)

# Loading images
battle_background = pygame.image.load("battle/battlebackground.png")
text_bar = pygame.transform.scale(pygame.image.load("battle/text_bar.png"), (800, 134))

# Loading battle buttons

p1_attacks_pos = (488, 460)
p1_attacks = ImgButton(p1_attacks_pos[0], p1_attacks_pos[1], 'battle/fight buttons.png', "p1_attack")

p1_backpack_pos = (656, 460)
p1_backpack = ImgButton(p1_backpack_pos[0], p1_backpack_pos[1], 'battle/fight buttons.png', "p1_backpack")

p1_chooses_pos = (488, 500)
p1_chooses_pokemon = ImgButton(p1_chooses_pos[0], p1_chooses_pos[1], 'battle/fight buttons.png', "p1_chose")

p1_runs_pos = (656, 500)
p1_runs = ImgButton(p1_runs_pos[0], p1_runs_pos[1], 'battle/fight buttons.png', "p1_run")

p2_attacks = ImgButton(636, 485, 'battle/fight buttons.png', "p2_attack")
p2_chooses_pokemon = ImgButton(636, 485, 'battle/fight buttons.png', "p2_chose")

# loading menu for player 1 and resizing it
fight_options = pygame.image.load("battle/fgt_options.png")
fight_options = pygame.transform.scale(fight_options, (get_width(fight_options) * 3, get_height(fight_options) * 3 - 10))

# grouping fight options for p1 in a list
p1_battle_buttons = [
    p1_attacks,
    p1_backpack,
    p1_chooses_pokemon,
    p1_runs
]

# grouping fight options positions for p1 on a list
p1_bb_positions = [
    p1_attacks_pos,
    p1_backpack_pos,
    p1_chooses_pos,
    p1_runs_pos
]

# loading and resizizng attack options menu
attack_options = pygame.image.load("battle/attack_menu.png")
attack_options = pygame.transform.scale(attack_options, (800, 124))

# creating attack buttons
attack1_pos = (42 , 447)
attack1 = ImgButton(attack1_pos[0], attack1_pos[1], "battle/attackoptions.png", "attack1")

attack2_pos = (274 , 447)
attack2 = ImgButton(attack2_pos[0], attack2_pos[1], "battle/attackoptions.png", "attack2")

attack3_pos = (42 , 492)
attack3 = ImgButton(attack3_pos[0], attack3_pos[1], "battle/attackoptions.png", "attack3")

attack4_pos = (274 , 492)
attack4 = ImgButton(attack4_pos[0], attack4_pos[1], "battle/attackoptions.png", "attack4")

# grouping them on a list

attack_options_positions = [
    attack1_pos,
    attack2_pos,
    attack3_pos,
    attack4_pos
]

attack_options_buttons = [
    attack1,
    attack2,
    attack3,
    attack4
]

# variable used on attack names
attack_name = 0

# Loading player 1 circle
p1_pad = pygame.image.load("battle/p1_pad.png")
p1_pad_x = 800
p1_pad_y = 355

# Loading player 2 circle
p2_pad = pygame.image.load("battle/p2_pad.png")
p2_pad_x = -447
p2_pad_y = 206

# Loading p1_animation
p1_animation = []
for num in range(0, 5):
    img = (pygame.image.load(f"battle/player1_animation/{num}.png"))
    resized_img = pygame.transform.scale( img , (((get_width(img) * 3)), (get_height(img) * 3)))
    p1_animation.append(resized_img)

p1_current_frame = 0
p1_char_x = 960
p1_char_y = 230

# setting hp bar initial coordinates
# player 2
bar1x = -110
bar1y = 100
# player 1
bar2x = 1000
bar2y = 290

# Loading p2 char
p2_charb = pygame.image.load(f"battle/p2_char.png")

resized_p2 = pygame.transform.scale(p2_charb, (152, 244))
p2_char_x = -320
p2_char_y = 30

# Function "write"
counter = 0

# text position
tx = 30
ty = 440

# alph variable used on pokémon fading animation
alph = 255
alph1 = 255

# setting variable used on p1 animation
actualp1frame = 0

# loading indicator
indicatr = pygame.transform.scale2x(pygame.image.load("battle/indicator.png"))
(600, 200)

# loading and resizing pokeballs
poke1 = pygame.image.load("battle/poke1.png")
poke1 = pygame.transform.scale(poke1, ((get_width(poke1) * 3), (get_height(poke1) * 3)))

poke2 = pygame.image.load("battle/poke2.png")
poke2 = pygame.transform.scale(poke2, ((get_width(poke2) * 3), (get_height(poke2) * 3)))

poke3 = pygame.image.load("battle/poke3.png")
poke3 = pygame.transform.scale(poke3, ((get_width(poke3) * 3), (get_height(poke3) * 3)))

# grouping them on a list
pokes = [
    poke1,
    poke2,
    poke3
]

# loading and resizing hp bars
hp1 = pygame.image.load("battle/barra_1.png")
hp1 = pygame.transform.scale( hp1 , (get_width(hp1) * 3, get_height(hp1) * 3))

hp2 = pygame.image.load("battle/barra_2.png")
hp2 = pygame.transform.scale( hp2 , (get_width(hp2) * 3, get_height(hp2) * 3))

# loading and resizing bar images
blackbar = pygame.image.load("battle/barra_sem_vida.png")
blackbar = pygame.transform.scale( blackbar , (get_width(blackbar) * 3, get_height(blackbar) * 3))

redbar = pygame.image.load("battle/vida_vermelha.png")
redbar = pygame.transform.scale( redbar , (144, get_height(redbar) * 3))

yellowbar = pygame.image.load("battle/vida_amarela.png")
yellowbar = pygame.transform.scale( yellowbar , (144, get_height(yellowbar) * 3))


# setting show_hp function
def show_hp():

    # setting variables
    player1_inbattle = player1.in_battle
    
    # setting p1 hp:

    # if player 1 pokémon in battle has been damaged
    if player1_inbattle.damage != 0:
        # defining black bar width
        blackbarwidth1 = player1_inbattle.damage // 144
        # resizing blackbar
        blackbar1 = pygame.transform.scale(blackbar, (blackbarwidth1, get_height(blackbar)))
        # printing to screen
        win.blit(blackbar1, (592 + 144 - blackbarwidth1, 347))

    # if player 1 pokémon actual hp >= 20% and <= 50% from it original hp
    if player1_inbattle.hp - player1_inbattle.damage >= (0.2 * player1_inbattle.hp) and player1_inbattle.hp - player1_inbattle.damage <= (0.5 * player1_inbattle.hp):
        win.blit(yellowbar, (592, 347))

    # if player 1 pokémon actual hp <= 20% and >= 0 from it original hp
    if player1_inbattle.hp - player1_inbattle.damage <= (0.2 * player1_inbattle.hp) and player1_inbattle.hp - player1_inbattle.damage >= 0:
        win.blit(redbar, (592, 347))

def write(text, indicator = False):
    global counter, tx, ty

    if counter <= len(text):
        text_letters = text[0:int(counter)]
        text_render = font2.render((text_letters), True, (255, 255, 255))
        text_rect = text_render.get_rect()
        text_rect.topleft = (tx, ty)
        win.blit(text_render, text_rect)   
        counter += 0.3

    else:
        text_letters = text[0:len(text)]
        text_render = font2.render((text_letters), True, (255, 255, 255))
        text_rect = text_render.get_rect()

        text_rect.topleft = (tx, ty)
        win.blit(text_render, text_rect)
        if indicator == True:
            win.blit(indicatr, (tx + text_rect[2] + 5, ty + text_rect[3] // 2 - 5))

# setting step variable used to determinate battle step
step = 0
# setting variable used on pokeball animation
pokeball_counter = 0

P1_turn = False
P2_turn = False

# setting next turn function
def next_turn():
    global P1_turn, P2_turn, cursor, counter

    # if p1 turn, change it to p2 turn
    if P1_turn == True:
        P1_turn = False
        P2_turn = True
    
    # if p2 turn, change it to p1 turn
    elif P2_turn == True:
        P2_turn = False
        P1_turn = True

    cursor = 0
    counter = 0

# counter used on p1 animation
p1_ani = 0

# counter used on p1 attacked pokémon animation
p1_attacked = 0

# variable used on setting damage pokémon
damaged = False

# variable used to determinate if its showing attack options for p1
attack_opt = False

# variable used to determinate who won
winner = "no one"

#________________________________________________________________________________________________________#
# 10. Main game loop:
showing = "opening"


while running:

    #________________________________________________________________________________________________________#

    # If showing opening:
    if showing == "opening":

        # backg = pygame.draw.rect(win, (255, 255, 255)) (fade animation) (w.i.p)

        # filling screen with black color
        win.fill(w.returnColor)

        # printing white flash pokémon effect to screen
        win.blit(flash, (0, flash_y))
        # flash animation (if flash y coordinate smaller or equal to 600 - screen limit - and flash y bigger than -100)
        if flash_y <= 600 and flash_y > -100:
            # print mold to screen
            win.blit(opening1, (0 , 0))
            # changing y flash value
            flash_y -= 10
    
        # if flash animation done
        if flash_y == -100:

            # fade charmander animation (while charmander alph smaller or equal to 255 (max alpha value))
            if charmander_alph <= 255:
                # setting charmander image alpha accorting to charmander_alph variable
                charmander1.set_alpha(int(charmander_alph))
                # printing b/w charmander to screen
                win.blit(charmander1, (395, 193))
                # increasing charmander image alpha by 0.5
                charmander_alph += 1

            # if charmander fade done
            else:
                
                # print opening background
                win.blit(opening2, (0, 0))
                # print colored charmander
                win.blit(charmander2, (395, 193))
                # print game title
                win.blit(pokepy1, (10, 15))
                # print battle simulator label
                win.blit(battle_simulator, (130, 245))

                # increasing 0.2 in "blink" variable (used on press start button animation)
                blink += 0.2

                # while blink value smaller or equal to 90:
                if blink <= 90:
                    # print press_start button to screen
                    win.blit(press_start, (86, 471))

                # if blink value bigger than 110
                if blink > 110:
                    # reset its value
                    blink = 0

        # Tracking events
        for event in pygame.event.get():
            
            # if quit, running = false and break the main loop
            if event.type == pygame.QUIT:
                running = False
                break
            
            # else, if a key pressed:
            elif event.type == pygame.KEYDOWN:

                # if pressed key == space bar
                if event.key == pygame.K_RETURN:

                    # play sound effect
                    pygame.mixer.Sound.play(plim)

                    # show menu
                    showing = "menu"
                    # break for loop
                    break
        
        # update display
        pygame.display.update()

    # If showing menu:
    if showing == "menu":

        # Setting cursor position:
        cursor_position_shifted = menu_bpositions[cursor]
        cursor_position = (
        cursor_position_shifted[0] + choose_button1.size[0] // 10,
        cursor_position_shifted[1] + choose_button1.size[1] // 2
        )

        # Printing images to screen
        for image in menu_images:
            win.blit(image[0], image[1])
        
        # variables used on main menu pokeballs (w.i.p)
        n1_pokes = len(player1.pokemon_list)
        n2_pokes = len(player2.pokemon_list)
        # for n1_pokes in range()

        # Tracking events
        for event in pygame.event.get():

            # If quit, stop the program
            if event.type == pygame.QUIT:
                running = False
                break

            # Tracking cursor
            if event.type == pygame.KEYDOWN:

                # Playing sound effect
                pygame.mixer.Sound.play(plim)

                if event.key == pygame.K_RIGHT and cursor != 4:
                    cursor += 1

                elif event.key == pygame.K_RIGHT and cursor == 4:
                    cursor -= 3

                elif event.key == pygame.K_LEFT:
                    cursor -= 1

                elif event.key == pygame.K_UP:
                    cursor -= 2

                elif event.key == pygame.K_DOWN:
                    if cursor == 3:
                        cursor += 1

                    elif cursor == 4:
                        cursor -= 4

                    else:
                        cursor += 2

                # Checking cursor limits:
                if cursor >= len(menu_bpositions):
                    cursor -= len(menu_bpositions)
                elif cursor < 0:
                    cursor += len(menu_bpositions)
                
                # if pressed key == spacebar
                if event.key == pygame.K_RETURN:

                    # for button in menu buttons list:
                    for button in menu_buttons:
                        # if cursor in button:
                        if cursor_position in button:

                            # if button function == "chooseP1"
                            if button.function == "chooseP1":
                                # show button function
                                showing = button.function
                                # Restarting cursor
                                cursor = 0
                                # continue main loop
                                continue
                            
                            # if button function == "chooseP2"
                            elif button.function == "chooseP2":
                                # show button function
                                showing = button.function
                                # Restarting cursor
                                cursor = 0
                                # continue main loop
                                continue
                            
                            # if button function == "startbattle"
                            elif button.function == "startBattle":
                                # if both players chose 4 pokémon
                                if all_set == True:
                                    # show button function
                                    showing = button.function
                                    # Restarting cursor
                                    cursor = 0
                                    # continue main loop
                                    continue
                            
                            # else, if button function is randomize for P1:
                            elif button.function == "randomizeP1":
                                # loop that set randomly 4 pokémon for player 1
                                for i in range(0, 4):
                                    player1.set_pokemon(random.choice(selectable_pokemon), i)

                            # else, if button function is randomize for P1:
                            elif button.function == "randomizeP2":
                                # loop that set randomly 4 pokémon for player 2
                                for i in range(0, 4):
                                    player2.set_pokemon(random.choice(selectable_pokemon), i)

        # if player 1 chose more than 4 pokémon
        if player1.poke_num > 4:
            # limit it to 4, redefining player1 number of pokémon
            player1.poke_num = 4
        
        # if player 2 chose more than 4 pokémon
        if player2.poke_num > 4:
            # limit it to 4, redefining player2 number of pokémon
            player2.poke_num = 4

        # for button in menu buttons list:
        for button in menu_buttons:
            # if cursor in button, print highlighted button
            if cursor_position in button:
                print_button(win, button, True)
            # else, if cursor not in button, print normal button
            else:
                print_button(win, button, False)

        # If Player 1 has already selected 4 Pokémon:
        if player1.poke_num == 4:
            # print all set warning to screen
            win.blit(allset, (70, 250))

        # If Player 2 has already selected 4 Pokémon:
        if player2.poke_num == 4:
            # print all set warning to screen
            win.blit(allset, (520, 250))

        # if player1 and player 2 has already selected each 4 pokémon, everything has been setted
        if player1.poke_num == 4 and player2.poke_num == 4:
            all_set = True
        
        # if not:
        else:
            # print gray star battle button to screen (sinalizing that the game can't start before each player choose 4 pokémon)
            start_battle_off = pygame.image.load("menu/start_battle_off.png")
            win.blit(start_battle_off, (start_battle.x, start_battle.y))

        # Updating display
        pygame.display.update()

    # If showing choose pokémon menu:
    if showing == "chooseP1" or showing == "chooseP2":

        # Setting Pokémon list:
        # For every button position in choose button positions list present in the break between "f" (first) and "l" (last)
        for position in choose_positions[0:8]:
            # Assigning "xc" variable value from position tuple (X)
            position[0] = xc
            # Assigning "yc" variable value from position tuple (y)
            position[1] = yc
            # Updating yc value (height)
            yc += 51
            # If yc exceed limit (469), reset it to initial value (112)
            if yc > 469:
                yc = 112

        # Setting cursor position:
        cursor_position_shifted = choose_positions[cursor]

        cursor_position = (
        cursor_position_shifted[0] + bulbasaur_button.size[0] // 10,
        cursor_position_shifted[1] + bulbasaur_button.size[1] // 2
        )

        # Printing images to screen:
        for image in choose_screen:
            win.blit(image[0], image[1])

        # If choosing for player 1
        if showing == "chooseP1":
            
            # Blitting player 1 character to screen
            win.blit((player1_sprites["choose"])[0], (player1_sprites["choose"])[1])

            # Blitting player 1 title to screen
            text(win, "Player 2", font_size2, 29, 313, (255, 255, 255))

            # Setting text position
            x = 47
            y = 376

            # For every name in player 1 choosen pokémon list:
            for pokemon in player1.pokemon_list:
                
                # If pokémon name == "" (not choosen yet)
                if pokemon == "":
                    # Blit "None" to screen
                    text(win, "None", font_size1, x, y, (255, 255, 255))
                    # Updating text position (height)
                    y += 36

                # Else:
                else:
                    # Blit pokémon name to screen
                    text(win, pokemon.name, font_size1, x, y, (255, 255, 255))
                    # Updating text position (height)
                    y += 36
    
        # If choosing for player 2
        elif showing == "chooseP2":

            # Blitting player 2 character to screen
            win.blit((player2_sprites["choose"])[0], (player2_sprites["choose"])[1])

            # Blitting player 2 title to screen
            text(win, "Player 2", font_size2, 29, 313, (255, 255, 255))

            # Setting choosen pokémon name position
            x = 47
            y = 376

            # For every pokémon name in player 2 choosen pokémon list:
            for pokemon in player2.pokemon_list:
                
                # If pokémon name == "" (not choosen yet)
                if pokemon == "":
                    # Blit "None" to screen
                    text(win, "None", font_size1, x, y, (255, 255, 255))
                    # Updating position (height)
                    y += 36
    
                # Else:
                else:
                    # Blit to screen pokémon name
                    text(win, pokemon.name, font_size1, x, y, (255, 255, 255))
                    # Updating position (height)
                    y += 36

        # Tracking events
        for event in pygame.event.get():

            # If quit, running = false and break the main loop
            if event.type == pygame.QUIT:
                running = False
                break

            # If a key pressed:
            if event.type == pygame.KEYDOWN:
                # Play sound effect
                pygame.mixer.Sound.play(plim)

                # If key pressed = right, reset cursor value
                if event.key == pygame.K_RIGHT:
                    cursor = 0

                # Else, if key = left, cursor = 8 (back button value)
                elif event.key == pygame.K_LEFT:
                    cursor = 8

                # Else, if key = up:
                elif event.key == pygame.K_UP:
                    # If cursor = 0, change it to 7 (go to the end of the list)
                    if cursor == 0:
                        cursor = 7
                    # Else, decrease 1 in cursor value
                    else:
                        cursor -= 1

                # Else, if key = down:
                elif event.key == pygame.K_DOWN:
                    # If cursor = 7 (showing last selectable pokémon)
                    if cursor == 7:
                        # Reset it (go back to the first selectabel pokémon)
                        cursor = 0
                    # Else, increase 1 in cursor value
                    else:
                        cursor += 1

                # Checking cursor limits:
                # If cursor equal or bigger than choose buttons positions list size (9)
                if cursor >= len(choose_positions):
                    # Decrease cursor value in choose buttons positions list size (9)
                    cursor -= len(choose_positions)
                
                # Else, if cursor value smaller than 0:
                elif cursor < 0:
                    # Increase cursor value in choose buttons positions list size (9)
                    cursor += len(choose_positions)

                # If enter key pressed
                if event.key == pygame.K_RETURN:
                    # For every button in choosing menu buttons list:
                    for button in choose_buttons:
                        # If cursor in button:
                        if cursor_position in button:
                            
                            # If button function = back:
                            if button.function == "back":
                                # Go back to menu
                                showing = "menu"
                                # Reset cursor value
                                cursor = 0
                                # Go to the loop's beginning
                                continue
                            
                            # Else:
                            else:
                                # If P1 choosing:
                                if showing == "chooseP1":
                                    player1.set_pokemon(button.pokemon, n1)
                                    n1 += 1
                                    if n1 >= 4:
                                        n1 = 0

                                # Else, if P2 choosing:
                                elif showing == "chooseP2":
                                    player2.set_pokemon(button.pokemon, n2)
                                    n2 += 1
                                    if n2 >= 4:
                                        n2 = 0
                
        # Setting pokémon buttons positions:
        # For every button in buttons list present in the break between "f" (first) and "l" (last):
        for button in choose_buttons[0:8]:
            # Set button x to 285 (standard x value)
            button.set_x = 285
            # Set button y to new_y value
            button.set_y = new_y
            # Updating new_y value (increasing by 51)
            new_y += 51
            # If new_y exceed limit (469), reset it to initial value (112)
            if new_y > 469:
                new_y = 112
        
        # Printing buttons:
        # For button in choose buttons list (from 0 to 7)
        for button in choose_buttons[0:8]:

            # If cursor in button, highlighted = true
            if cursor_position in button:
                # Print button and selected pokémon stats
                print_button(win, button, True)
                print_stats(button)

            # Else, highlighted = false
            else:
                # Print button
                print_button(win, button, False)

        # Printing back button:
        # If cursor in back button, highlighted = True
        if cursor_position in back:
            print_button(win, back, True)
        # Else, highlighted = False
        else:
            print_button(win, back, False)

        # Updating display
        pygame.display.update()

    # If showing battle
    if showing == "startBattle":

        # If showing battle introduction
        if P1_turn == False and P2_turn == False:

            # printing background
            win.blit(battle_background, (0, 0))

            # Animating P2 pad (if player 2's pad has not reached its final x coordinate)
            if p2_pad_x < 373:
                # print it to screen
                win.blit(p2_pad, (p2_pad_x, p2_pad_y))
                # increase its x value by 5
                p2_pad_x += 5
            # if player 2's pad has reached its final x coordinate
            else:
                # print it to screen at its final coordinates
                win.blit(p2_pad, (p2_pad_x, p2_pad_y))
                
            # Animating P2 char (if player 2's character has not reached its final x coordinate)
            if p2_char_x < 510:
                # print it to screen
                win.blit(resized_p2, (p2_char_x, p2_char_y))
                # increase its x value by 5
                p2_char_x += 5
            # if player 2's character has reached its final x coordinate
            else:
                # print it to screen at its final coordinates
                win.blit(resized_p2, (p2_char_x, p2_char_y))

            # Animating P1 pad (if player 1's pad has not reached its final x coordinate)
            if p1_pad_x > 0:
                # print it to screen
                win.blit(p1_pad, (p1_pad_x, p1_pad_y))
                # decrease its x value by 5
                p1_pad_x -= 5
            # if player 1's pad has reached its final x coordinate
            else:
                # print it to screen at its final coordinates
                win.blit(p1_pad, (p1_pad_x, p1_pad_y))     

            # Animating P1 char (if player 1's character has not reached its final x coordinate)
            if p1_char_x > 200:
                # print it to screen
                win.blit(p1_animation[0], (p1_char_x, p1_char_y))
                # decrease its x value by 5
                p1_char_x -= 5
            # if player 1's character has reached its final x coordinate
            else:
                # print it to screen at its final coordinates
                win.blit(p1_animation[0], (p1_char_x, p1_char_y))

            # printing text bar to screen
            win.blit(text_bar, (0, 419))

            # writing intro text
            write("PLAYER 2 would like to battle!", True)
            
            # setting first player 1 playable pokémon (the first one that was chosen)
            p1_1poke = player1.pokemon_list[0]
            # setting first player 2 playable pokémon (the first one that was chosen)
            p2_1poke = player2.pokemon_list[0]

            # player 2 has the first move
            show = p2_chooses_pokemon.function

            # using show_hp function
            show_hp()

        # If P2 turn
        if P2_turn == True:
            
            # resizing pokémon images
            bigger_poke2 = pygame.transform.scale( (player2.in_battle).front_img , ( (get_width((player2.in_battle).front_img) * 3, get_height((player2.in_battle).front_img) * 3)))

            # determining if pokemon is fainted
            if (player2.in_battle).damage >= player2.in_battle.hp:
                player2.in_battle.set_state = "fainted"

            # if player 2 choosing pokémon
            if show == p2_chooses_pokemon.function:
                
                # determining player 2 pokémon (w.i.p)

                # printing battle interface images
                win.blit(battle_background, (0, 0))
                win.blit(p1_pad, (p1_pad_x, p1_pad_y))
                win.blit(p2_pad, (p2_pad_x, p2_pad_y))
                win.blit(resized_p2, (p2_char_x, p2_char_y))
                win.blit(p1_animation[0], (p1_char_x, p1_char_y))
                win.blit(text_bar, (0, 419))

                # writing message
                write(f"PLAYER 2 sent out {(player2.in_battle).name}!")
                
                # animating player 2 pokémon hp bar
                # if player 2's hp bar has not reached its final x coordinate
                if bar1x <= 100:
                    # print it to screen
                    win.blit(hp1, (bar1x, bar1y))
                    # increase hp bar x coordinate in 3
                    bar1x += 3
                # else:
                else:
                    # print it to screen at its final coordinates
                    win.blit(hp1, (bar1x, bar1y))

                # printing pokémon name
                name = font_size1.render((player2.in_battle).name, True, (64, 64, 64))
                nameRect = name.get_rect()
                nameRect.topleft = (bar1x + 20 , bar1y + 10)
                win.blit(name, nameRect)

                # printing pokémon gender symbol
                symbol = pygame.transform.scale((pygame.image.load(f"choose_interface/{(player2.in_battle).gender}.png")), (15, 24))
                win.blit(symbol, (bar1x + nameRect[2] + 25, bar1y + 10) )
                
                # printing level
                level = font_size1.render(str(player2.in_battle.level), True, (64, 64, 64))
                levelRect = level.get_rect()
                levelRect.topleft = (bar1x + 250 , bar1y + 10)
                win.blit(level, levelRect)

                # resizing pokémon images
                bigger_colored_poke2 = pygame.transform.scale( (player2.in_battle).colored_imgf , ( (get_width((player2.in_battle).colored_imgf) * 3, get_height((player2.in_battle).colored_imgf) * 3)))
                
                # pokémon showing up and fading animation                
                # if pink pokémon image alpha bigger or equal to 0 (while animation not done):
                if alph >= 0:
                    # print normal pokémon to screen
                    win.blit(bigger_poke2, (510, 80))
                    # setting colored pokémon image alpha
                    bigger_colored_poke2.set_alpha(alph)
                    # printing colored pokémon image to screen
                    win.blit(bigger_colored_poke2, (510, 80))
                    # decreasing alph value by 3
                    alph -= 3
                # if animation done:
                else:
                    # print normal pokémon to screen
                    win.blit(bigger_poke2, (510, 80))

                # animating player 2 (leaving from screen)
                # if p2 character x coordinate bigger ot equal to 510 (player 2 has not left from screen yet) and smaller than 1000 (ending of animation):
                if p2_char_x >= 510 and p2_char_x < 1000:
                    # print it to screen
                    win.blit(resized_p2, (p2_char_x, p2_char_y))
                    # increase player 2 x coordinate by 5
                    p2_char_x += 5

                # animating pokémon pokéball (while counter smaller or equal to 2.9):
                if pokeball_counter <= 2.9:
                    # setting pokeball x coordinate based on player 2 pad mid
                    middle = ((get_width(p2_pad) - get_width(pokes[0])) // 2) + p2_pad_x
                    # printing pokeball from pokeballs list (index according to pokeball counter variable)
                    win.blit(pokes[int(pokeball_counter)], (middle, 220))
                    # increase pokeball counter in 0.08
                    pokeball_counter += 0.08

                # choosing player 2 first move
                p2attack = (player2.in_battle).set_currently_attack(random.randint(0, 3))

            # if player 2 attacking
            if show == p2_attacks.function:
                
                # filling screen
                win.fill(w.returnColor)

                # printing battle interface images to screen
                win.blit(battle_background, (0, 0))
                win.blit(p1_pad, (p1_pad_x, p1_pad_y))
                win.blit(p2_pad, (p2_pad_x, p2_pad_y))

                # printing in battle pokémon
                win.blit(bigger_poke2, (510, 80))

                # printing player 2 hp bar and informations
                win.blit(hp1, (bar1x, bar1y))
                win.blit(name, nameRect)
                win.blit(symbol, (bar1x + nameRect[2] + 25, bar1y + 10) )
                win.blit(level, levelRect)

                # printing player 1 hp bar and informations
                win.blit(hp2, (bar2x, bar2y))
                win.blit(name1, name1Rect)
                win.blit(symbol1, (bar2x + name1Rect[2] + 50, bar2y + 20) )
                win.blit(level1, level1Rect)

                # resizing and animating p1 pokémon image
                bigger_poke1 = pygame.transform.scale( (player1.in_battle).back_img , ( (get_width((player1.in_battle).back_img) * 3, get_height((player1.in_battle).back_img) * 3)))

                # if p1 counter smaller or equal to 100
                if p1_attacked < 100:
                    # increase p1 counter by 2
                    p1_attacked += 2

                # if p1_attacked divisible by 10
                if p1_attacked % 10 == 0:
                    # print pokemon
                    win.blit(bigger_poke1, (120, 300))

                # printing text bar and writing the message
                win.blit(text_bar, (0, 419))
                write(f"Foe {(player2.in_battle).name} used {((player2.in_battle).currently_attack).name}!")
                
                # setting player 1 pokémon damage
                # variable used to set damage once
                if damaged == False:
                    (player1.in_battle).damage = ((player2.in_battle).currently_attack).damage
                    damaged = True
                
                # using show_hp function
                show_hp()

        # If P1 turn
        if P1_turn == True:
            
            # determining if pokemon is fainted
            if (player1.in_battle).damage >= player1.in_battle.hp:
                player1.in_battle.set_state = "fainted"

            # resizing pokémon image
            bigger_poke1 = pygame.transform.scale( (player1.in_battle).back_img , ( (get_width((player1.in_battle).back_img) * 3, get_height((player1.in_battle).back_img) * 3)))

            # if player 1 choosing pokémon
            if show == p1_chooses_pokemon.function:

                # filling window
                win.fill(w.returnColor)

                # printing battle interface images
                win.blit(battle_background, (0, 0))
                win.blit(p1_pad, (p1_pad_x, p1_pad_y))
                win.blit(p2_pad, (p2_pad_x, p2_pad_y))
                win.blit(bigger_poke2, (510, 80))
                win.blit(hp1, (bar1x, bar1y))
                win.blit(name, nameRect)
                win.blit(symbol, (bar1x + nameRect[2] + 25, bar1y + 10) )
                win.blit(level, levelRect)
                
                # while p1_char_x on screen
                if p1_char_x <= 230 and p1_char_x > -200:
                    # printing images to screen
                    win.blit(p1_animation[int(actualp1frame)], (p1_char_x, p1_char_y))
                    # changing p1 animation frame 
                    actualp1frame += 0.2
                    # moving p1 character
                    p1_char_x -= 5

                # if actualp1frame bigger or equal to 4 (len(p1_animation) - 1), redefine it
                if actualp1frame >= 4:
                    actualp1frame = 4

                # animating player 1 pokémon hp bar
                # if player 1's hp bar has not reached its final x coordinate
                if bar2x >= 450:
                    # print it to screen
                    win.blit(hp2, (bar2x, bar2y))
                    # increase hp bar x coordinate in 3
                    bar2x -= 8
                # else:
                else:
                    # print it to screen at its final coordinates
                    win.blit(hp2, (bar2x, bar2y))

                # printing pokémon name
                name1 = font_size1.render((player1.in_battle).name, True, (64, 64, 64))
                name1Rect = name1.get_rect()
                name1Rect.topleft = (bar2x + 45 , bar2y + 20)
                win.blit(name1, name1Rect)

                # printing pokémon gender symbol
                symbol1 = pygame.transform.scale((pygame.image.load(f"choose_interface/{(player1.in_battle).gender}.png")), (15, 24))
                win.blit(symbol1, (bar2x + name1Rect[2] + 50, bar2y + 20) )
                
                # printing level
                level1 = font_size1.render(str(player1.in_battle.level), True, (64, 64, 64))
                level1Rect = level1.get_rect()
                level1Rect.topleft = (bar2x + 280 , bar2y + 20)
                win.blit(level1, level1Rect)

                # resizing pokémon images
                bigger_colored_poke1 = pygame.transform.scale( (player1.in_battle).colored_imgb , ( (get_width((player1.in_battle).colored_imgb) * 3, get_height((player1.in_battle).colored_imgb) * 3)))
                
                # pokémon showing up and fading animation                
                # if pink pokémon image alpha bigger or equal to 0 (while animation not done):
                if alph1 >= 0:
                    # print normal pokémon to screen
                    win.blit(bigger_poke1, (120, 300))
                    # setting colored pokémon image alpha
                    bigger_colored_poke1.set_alpha(alph1)
                    # printing colored pokémon image to screen
                    win.blit(bigger_colored_poke1, (120, 300))
                    # decreasing alph value by 3
                    alph1 -= 3

                # if animation done:
                else:
                    # print normal pokémon to screen
                    win.blit(bigger_poke1, (120, 300))

                # animating pokémon pokéball (while counter smaller or equal to 2.9):
                if pokeball_counter <= 2.9:
                    # setting pokeball x coordinate based on player 2 pad mid
                    middle = ((get_width(p1_pad) - get_width(pokes[0])) // 2) + p1_pad_x
                    # printing pokeball from pokeballs list (index according to pokeball counter variable)
                    win.blit(pokes[int(pokeball_counter)], (middle, 220))
                    # increase pokeball counter in 0.08
                    pokeball_counter += 0.08

                win.blit(text_bar, (0, 419))
                # writing message
                write(f"Go! {(player1.in_battle).name}!")

                # using show_hp function
                show_hp()

            # if player 1 attacking
            if show == p1_attacks.function:

                # if not showing attack options 
                if attack_opt == False:
                    # Setting cursor position:
                    cursor_position_shifted = p1_bb_positions[cursor]

                    cursor_position = (
                    cursor_position_shifted[0] + p1_attacks.size[0] // 10,
                    cursor_position_shifted[1] + p1_attacks.size[1] // 2
                    )

                # filling window
                win.fill(w.returnColor)

                # printing battle interface images
                win.blit(battle_background, (0, 0))
                win.blit(p1_pad, (p1_pad_x, p1_pad_y))
                win.blit(p2_pad, (p2_pad_x, p2_pad_y))
                win.blit(bigger_poke1, (120, 300))
                win.blit(hp1, (bar1x, bar1y))
                win.blit(name, nameRect)
                win.blit(symbol, (bar1x + nameRect[2] + 25, bar1y + 10) )
                win.blit(level, levelRect)
                win.blit(hp2, (bar2x, bar2y))
                win.blit(name1, name1Rect)
                win.blit(symbol1, (bar2x + name1Rect[2] + 50, bar2y + 20) )
                win.blit(level1, level1Rect)
                win.blit(bigger_poke2, (510, 80))

                # printing text bar and writing the message
                win.blit(text_bar, (0, 419))
                write(f"What will {player1.in_battle.name} do?")

                # printing fight options
                win.blit(fight_options, (440, 419))

                # using show_hp function
                show_hp()

                # if showing attack options
                if attack_opt == True:

                    # tracking cursor
                    cursor_position_shifted = attack_options_positions[cursor]

                    cursor_position = (
                    cursor_position_shifted[0] + attack1.size[0] // 10,
                    cursor_position_shifted[1] + attack1.size[1] // 5
                    )

                    # printing menu
                    win.blit(attack_options, (0, 419))

                    # setting button functions as attack names
                    # if attack name value smaller than 3 (max index number on player 1 moves)
                    if attack_name < 3:
                        # for button in attack options buttons
                        for button in attack_options_buttons:
                            # setting function by attack name
                            button.set_function = ((player1.in_battle).moves[attack_name])
                            # increasing attack name variable by 1
                            attack_name += 1

                    # printing attack names
                    for button in attack_options_buttons:
                        text(win, (button.function).name, font_size3, button.x, button.y, (64, 64, 64))

        
        # Tracking events
        for event in pygame.event.get():

            # if quit, running = false and break the main loop
            if event.type == pygame.QUIT:
                running = False
                break
            
            # If a key pressed
            if event.type == pygame.KEYDOWN:
            
                # Play sound effect
                pygame.mixer.Sound.play(plim)

                # Checking cursor limits:
                if cursor >= len(p1_battle_buttons):
                    cursor -= len(p1_battle_buttons)
                elif cursor < 0:
                    cursor += len(p1_battle_buttons)
                
                if event.key == pygame.K_DOWN:
                    cursor += 2
                
                if event.key == pygame.K_RIGHT:
                    cursor += 1

                if event.key == pygame.K_UP:
                    cursor -= 2

                if event.key == pygame.K_LEFT:
                    cursor -= 1

                if event.key == pygame.K_RETURN:
                    
                    # If showing introduction and animation is over
                    if P1_turn == False and P2_turn == False:
                        if p2_char_x == 510:
                            # next step
                            P2_turn = True
                    
                    # if player 1 turn
                    if P1_turn == True:
                        
                        # if player 1 pokémon didn't fainted yet
                        if player1.in_battle.state != "fainted":

                            # if bar animation done and p1 chose
                            if bar2x < 450 and show == p1_chooses_pokemon.function:
                                # it's p2 time to attack
                                show = p2_attacks.function
                                next_turn()

                            # if a button pressed
                            for button in p1_battle_buttons:
                                if cursor_position in button:

                                    # if pressed button == run:
                                    if button.function == p1_runs.function:
                                        winner = player2

                                    # if pressed button == fight:
                                    if button.function == p1_attacks.function:
                                        # show attack options
                                        attack_opt = True

                            # if a button pressed on moves list
                            for button in attack_options_buttons:
                                if cursor_position in button:
                                    # p2 were damaged
                                    damaged = True
                                    # reseting player 1 pokémon animation variable
                                    p1_attacked = 0
                                    # setting currently attack
                                    (player1.in_battle).set_currently_attack = button.function
                                    
                                    # don't show attack options
                                    attack_opt = False

                            # if p1 attacked
                            if damaged == True:
                                # it's p2 time to attack
                                show = p2_attacks.function
                                # reset damaged variable
                                damaged = False
                                next_turn()

                        else:
                            winner = player2

                    # if player 2 turn
                    if P2_turn == True:
                        
                        # if player 2 pokémon didn't fainted yet
                        if player2.in_battle.state != "fainted":
                            # if bar animation done and p2 chose
                            if bar1x >= 100 and show == p2_chooses_pokemon.function:
                                # it's p1 time to choose
                                show = p1_chooses_pokemon.function
                                next_turn()
                            
                            # if p2 attacked
                            if damaged == True:
                                # it's p1 time to attack
                                show = p1_attacks.function
                                # reset damaged variable
                                damaged = False
                                next_turn()
                        else:
                            winner = player1

        # if showing p1 fight options
        if show == p1_attacks.function and attack_opt == False:
            # print buttons
            for button in p1_battle_buttons:
                # If cursor in button, highlighted = true
                if cursor_position in button:
                    # Print button
                    print_button(win, button, True)
                # Else, highlighted = false
                else:
                    # Print button
                    print_button(win, button)

        # if showing attack options
        if show == p1_attacks.function and attack_opt == True:
            # print buttons
            for button in attack_options_buttons:
                # If cursor in button, highlighted = true
                if cursor_position in button:
                    # Print button
                    print_button(win, button, True)
                # Else, highlighted = false
                else:
                    # Print button
                    print_button(win, button)

        # if p1 won
        if winner == player1:
            win.fill((255, 255, 255))
            text(win, "PLAYER 1 WON!, CONGRATULATIONS!", font_size2, 50, 180, (64, 64, 64))

        # if p2 won
        if winner == player2:
            win.fill((255, 255, 255))
            text(win, "PLAYER 2 WON! GOOD LUCK NEXT TIME!", font_size1, 20, 180, (64, 64, 64))

        pygame.display.update()
        
        
# Quitting pygame
pygame.quit()
