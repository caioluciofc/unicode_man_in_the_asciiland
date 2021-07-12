import os
import colors
import click
import math
import monsters
import random
import platform

SCREENWIDTH = 100
SCREENHEIGHT = 20
CAMERAWIDTH = 40
SPACEBETWEENLINESCAMERA = int(SCREENWIDTH/2 - (CAMERAWIDTH)) - 1
GAMENAME = "UNICODE MAN IN THE ASCIIVERSE!"
UNICODEMAN = '\033[93m☺\033[0m'
user_level = 1
user_str = 5
user_dex = 1
user_def = 1
user_health = 100
user_status = "Good"

walls = ["#", "@", "|", "/", "-", "8", "\\", "_", "\033[01m\033[31m+\033[0m",
         "\033[01m\033[31m§\033[0m", "\033[01m\033[31mЖ\033[0m"]

print(platform.system())

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
    player_stats = f"Level {user_level} STR {user_str} DEX {user_dex} DEF {user_def}"
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


def change_scene(file, unicode_y, unicode_x):
    global game_map
    with open(file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            this_line = []
            for char in line:
                this_line.append(char)
            game_map.append(this_line)


def use_item(item):
    global user_health
    global user_dex
    global user_def
    # Red Cross +
    if item == "\033[01m\033[31m+\033[0m":
        user_health += 20
    # Weird DEX Symbol
    elif item == "\033[01m\033[31m§\033[0m":
        user_dex += 2
    # Weird INT Symbol
    elif item == "\033[01m\033[31mЖ\033[0m":
        user_def += 2


def monster_action(monster):
    # global unicode_man_x
    # global unicode_man_y
    # global game_map
    global user_health
    if monster.health > 0:
        monster_path = monster.calculate_path(unicode_man_y, unicode_man_x)
        if monster_path[0] == unicode_man_y and monster_path[1] == unicode_man_x:
            damage = monster.attack_player(user_def)
            user_health -= damage
        elif game_map[monster_path[0]][monster_path[1]] not in walls and game_map[monster_path[0]][monster_path[1]] != UNICODEMAN:
            game_map[monster.y][monster.x] = '.'
            monster_1.walk_to_player(monster_path[0], monster_path[1])


def grab_item(items):
    if game_map[unicode_man_y + 1][unicode_man_x] in items:
        use_item(game_map[unicode_man_y + 1][unicode_man_x])
        game_map[unicode_man_y + 1][unicode_man_x] = '.'
    elif game_map[unicode_man_y - 1][unicode_man_x] in items:
        use_item(game_map[unicode_man_y - 1][unicode_man_x])
        game_map[unicode_man_y - 1][unicode_man_x] = '.'
    elif game_map[unicode_man_y][unicode_man_x + 1] in items:
        use_item(game_map[unicode_man_y][unicode_man_x + 1])
        game_map[unicode_man_y][unicode_man_x + 1] = '.'
    elif game_map[unicode_man_y][unicode_man_x - 1] in items:
        use_item(game_map[unicode_man_y][unicode_man_x - 1])
        game_map[unicode_man_y][unicode_man_x - 1] = '.'
    elif game_map[unicode_man_y + 1][unicode_man_x + 1] in items:
        use_item(game_map[unicode_man_y + 1][unicode_man_x + 1])
        game_map[unicode_man_y + 1][unicode_man_x + 1] = '.'
    elif game_map[unicode_man_y + 1][unicode_man_x - 1] in items:
        use_item(game_map[unicode_man_y + 1][unicode_man_x - 1])
        game_map[unicode_man_y + 1][unicode_man_x - 1] = '.'
    elif game_map[unicode_man_y - 1][unicode_man_x + 1] in items:
        use_item(game_map[unicode_man_y - 1][unicode_man_x + 1])
        game_map[unicode_man_y - 1][unicode_man_x + 1] = '.'
    elif game_map[unicode_man_y - 1][unicode_man_x - 1] in items:
        use_item(game_map[unicode_man_y - 1][unicode_man_x - 1])
        game_map[unicode_man_y - 1][unicode_man_x - 1] = '.'


def attack_monster(monster, monsters_array):
    d6_roll = random.randint(1, 7)
    monster.health -= ((d6_roll * user_str)/2)-monster_1.defense
    if monster.health <= 0:
        print(monster_1.y, "   ", monster_1.x)
        game_map[monster.y][monster.x] = '.'
        monsters_array.remove(monster)
        print("Monster is dead")


monster_1 = monsters.Monster(100, "\033[35m@\033[0m", 7, 20, 60)
monster_2 = monsters.Monster(100, "\033[35mO\033[0m", 7, 20, 55)
monster_3 = monsters.Monster(100, "\033[35mM\033[0m", 7, 20, 65)
monster_4 = monsters.Monster(100, "\033[35mN\033[0m", 7, 20, 45)
monster_5 = monsters.Monster(100, "\033[35mX\033[0m", 7, 20, 40)

monsters_array = [monster_1, monster_2, monster_3, monster_4, monster_5]

monster_list = []

for monster in monsters_array:
    monster_list.append(monster.char)
    walls.append(monster.char)


print(monster_list)

game_on = False

start_game = input("DO YOU WANT TU PLAY?")

if start_game.upper() == "YES" or start_game.upper() == "Y":
    game_on = True

unicode_man_y, unicode_man_x = 20, 50
game_map[22][55] = "\033[01m\033[31m+\033[0m"
game_map[23][55] = "\033[01m\033[31m§\033[0m"
game_map[24][55] = "\033[01m\033[31mЖ\033[0m"
items = ["\033[01m\033[31m+\033[0m",
         "\033[01m\033[31m§\033[0m", "\033[01m\033[31mЖ\033[0m"]


while game_on:
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    for monster in monsters_array:
        if monster.health > 0:
            game_map[monster.y][monster.x] = monster.char
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
        grab_item(items)
        for monster in monsters_array:
            if abs((unicode_man_x - monster.x) + (unicode_man_y - monster.y)) == 1:
                attack_monster(monster, monsters_array)
                break
    else:
        old_tile = old_tile
        game_map[unicode_man_y][unicode_man_x] = UNICODEMAN
        continue
    for monster in monsters_array:
        old_y = monster.y
        old_x = monster.x
        action = monster.monster_action(
            unicode_man_y, unicode_man_x, user_def, walls, game_map)
        if action[0] == "wlk":
            game_map[old_y][old_x] = "."
        if action[0] == "atk":
            user_health -= action[1]
    if user_health <= 0:
        game_on = False

print("Game Over")
