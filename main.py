import emoji
import os
import colors
import click
import math
import interactable

SCREENWIDTH = 100
SCREENHEIGHT = 20
CAMERAWIDTH = 40
SPACEBETWEENLINESCAMERA = int(SCREENWIDTH/2 - (CAMERAWIDTH)) - 1
GAMENAME = "UNICODE MAN IN THE ASCIIVERSE!"
UNICODEMAN = '\033[93m☺\033[0m'
user_level = 1
user_str = 1
user_dex = 1
user_int = 1
user_health = 100
user_status = "Good"

walls = ["#", "@", "|", "/", "-", "8", "\\", "_"]
game_map = []
with open('map.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        this_line = []
        for char in line:
            this_line.append(char)
        game_map.append(this_line)


def camera(gamemap, y, x):
    print("|", end="")
    for k in range(0, SPACEBETWEENLINESCAMERA):
        print(" ", end="")
    for i in range(x-CAMERAWIDTH - 1, x+CAMERAWIDTH + 1):
        print("@", end="")
    for l in range(0, SPACEBETWEENLINESCAMERA):
        print(" ", end="")
    print("|")
    if y - int((SCREENHEIGHT / 2)) <= 0:
        range_y_1 = 0
        range_y_2 = SCREENHEIGHT
    elif y + int((SCREENHEIGHT / 2)) >= len(game_map):
        range_y_1 = len(game_map) - SCREENHEIGHT
        range_y_2 = len(game_map)
    else:
        range_y_1 = y - int((SCREENHEIGHT / 2))
        range_y_2 = y + int((SCREENHEIGHT / 2))
    if x-CAMERAWIDTH <= 0:
        range_x_1 = 0
        range_x_2 = CAMERAWIDTH * 2
    elif x+CAMERAWIDTH >= len(game_map[0]):
        range_x_1 = (len(game_map[0]) - CAMERAWIDTH * 2) - 1
        range_x_2 = len(game_map[0]) - 1
    else:
        range_x_1 = x - CAMERAWIDTH
        range_x_2 = x + CAMERAWIDTH
    for i in range(range_y_1, range_y_2):
        print("|", end="")
        for k in range(0, SPACEBETWEENLINESCAMERA):
            print(" ", end="")
        print("@", end="")
        for j in range(range_x_1, range_x_2):
            print(gamemap[i][j], end="")
        print("@", end="")
        for l in range(0, SPACEBETWEENLINESCAMERA):
            print(" ", end="")
        print("|")
    print("|", end="")
    for k in range(0, SPACEBETWEENLINESCAMERA):
        print(" ", end="")
    for i in range(x-CAMERAWIDTH - 1, x+CAMERAWIDTH + 1):
        print("@", end="")
    for l in range(0, SPACEBETWEENLINESCAMERA):
        print(" ", end="")
    print("|")


def gameScreen(gamemap, y, x):
    player_status = f"Health {user_health} Status: {user_status}"
    player_stats = f"Level {user_level} STR {user_str} DEX {user_dex} INT {user_int}"
    print("/", end="")
    for i in range(0, SCREENWIDTH):
        print('-', end="")
    print("\\")
    game_name_len = len(GAMENAME)
    print("|", end="")
    for i in range(0, int((SCREENWIDTH/2) - (game_name_len/2))):
        print(' ', end="")
    print(GAMENAME, end="")
    for i in range(0, int((SCREENWIDTH/2) - (game_name_len/2))):
        print(' ', end="")
    print("|")
    camera(gamemap, y, x)
    print("|", end="")
    for i in range(0, SCREENWIDTH):
        print(' ', end="")
    print("|")
    print("|", end="")
    for i in range(0, 10):
        print(' ', end="")
    print(player_stats, end="")
    for i in range(0, SCREENWIDTH - 10 - len(player_stats)):
        print(' ', end="")
    print("|")
    print("|", end="")
    for i in range(0, 10):
        print(' ', end="")
    print(player_status, end="")
    for i in range(0, SCREENWIDTH - 10 - len(player_status)):
        print(' ', end="")
    print("|")
    print("|", end="")
    for i in range(0, SCREENWIDTH):
        print(' ', end="")
    print("|")
    print("\\", end="")
    for i in range(0, SCREENWIDTH):
        print('-', end="")
    print("/", end="")
    print("\n", end="")
    print(x)
    print(y)


def interactables_insert(interactables_array):
    characters_dict = {}
    for interactable in interactables_array:
        if interactable.is_used == False:
            characters_dict[interactable.sprite] = interactable
            game_map[interactable.y][interactable.x] = interactable.sprite
    return characters_dict


game_on = False

start_game = input("DO YOU WANT TU PLAY?")

if start_game.upper() == "YES" or start_game.upper() == "Y":
    game_on = True

unicode_man_y, unicode_man_x = 20, 50
health_item = interactable.Interactable(22, 55, "\033[01m\033[31m+\033[0m")
interactables = [health_item]

while game_on:
    os.system('cls')
    interactables_map = interactables_insert(interactables)
    print(interactables_map)
    if game_map[unicode_man_y][unicode_man_x] == UNICODEMAN:
        pass
    else:
        old_tile = game_map[unicode_man_y][unicode_man_x]
        game_map[unicode_man_y][unicode_man_x] = UNICODEMAN
    gameScreen(game_map, unicode_man_y, unicode_man_x)
    what_do_you_do = click.getchar()
    if what_do_you_do == "a":
        if game_map[unicode_man_y][unicode_man_x - 1] in walls:
            continue
        else:
            game_map[unicode_man_y][unicode_man_x] = old_tile
            unicode_man_y, unicode_man_x = unicode_man_y, unicode_man_x - 1
    elif what_do_you_do == "d":
        if game_map[unicode_man_y][unicode_man_x + 1] in walls:
            continue
        else:
            game_map[unicode_man_y][unicode_man_x] = old_tile
            unicode_man_y, unicode_man_x = unicode_man_y, unicode_man_x + 1
    elif what_do_you_do == "w":
        if game_map[unicode_man_y - 1][unicode_man_x] in walls:
            continue
        else:
            game_map[unicode_man_y][unicode_man_x] = old_tile
            unicode_man_y, unicode_man_x = unicode_man_y - 1, unicode_man_x
    elif what_do_you_do == "s":
        if game_map[unicode_man_y + 1][unicode_man_x] in walls:
            continue
        else:
            game_map[unicode_man_y][unicode_man_x] = old_tile
            unicode_man_y, unicode_man_x = unicode_man_y + 1, unicode_man_x
    elif what_do_you_do == " ":
        if game_map[unicode_man_y + 1][unicode_man_x] in interactables_map or \
           game_map[unicode_man_y - 1][unicode_man_x] in interactables_map or \
           game_map[unicode_man_y][unicode_man_x + 1] in interactables_map or \
           game_map[unicode_man_y][unicode_man_x - 1] in interactables_map or \
           game_map[unicode_man_y + 1][unicode_man_x + 1] in interactables_map or \
           game_map[unicode_man_y + 1][unicode_man_x - 1] in interactables_map or \
           game_map[unicode_man_y - 1][unicode_man_x + 1] in interactables_map or \
           game_map[unicode_man_y - 1][unicode_man_x - 1] in interactables_map:
            game_map[interactables_map["\033[01m\033[31m+\033[0m"]
                     .y][interactables_map["\033[01m\033[31m+\033[0m"].x] = '.'
            user_health += 100
            health_item.health_up()
    else:
        old_tile = old_tile
        game_map[unicode_man_y][unicode_man_x] = UNICODEMAN
        continue
