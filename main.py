import emoji
import os
import colors

game_map = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
             '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '.', '.', '.', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
             ' ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             ' ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             ' ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.',
             ' ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
             '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
            ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#',
             '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]


def gameScreen(gamemapline):
    print("/", end="")
    for i in range(0, 100):
        print('-', end="")
    print("\\", end="")
    print("\n", end="")
    print("|", end="")
    for i in range(0, 100):
        print(' ', end="")
    print("|")
    for line in gamemapline:
        print("|", end="")
        for i in range(0, 30):
            print(" ", end="")
        for tile in line:
            print(tile, end="")
        for i in range(0, 40):
            print(" ", end="")
        print("|")
    print("|", end="")
    for i in range(0, 100):
        print(' ', end="")
    print("|")
    print("|", end="")
    for i in range(0, 100):
        print(' ', end="")
    print("|")
    print("|", end="")
    for i in range(0, 100):
        print(' ', end="")
    print("|")
    print("\\", end="")
    for i in range(0, 100):
        print('-', end="")
    print("/", end="")
    print("\n", end="")


unicode_man = 'C'

game_on = False

start_game = input("DO YOU WANT TU PLAY?")

if start_game == "Yes" or start_game == "Y":
    game_on = True

unicode_man_y, unicode_man_x = 3, 14

while game_on:
    os.system('cls')
    old_tile = game_map[unicode_man_y][unicode_man_x]
    game_map[unicode_man_y][unicode_man_x] = unicode_man
    gameScreen(game_map)

    what_do_you_do = input("ML, MR, MU, MD")
    if what_do_you_do == "ML":
        game_map[unicode_man_y][unicode_man_x] = old_tile
        unicode_man_y, unicode_man_x = unicode_man_y, unicode_man_x - 1
    elif what_do_you_do == "MR":
        game_map[unicode_man_y][unicode_man_x] = old_tile
        unicode_man_y, unicode_man_x = unicode_man_y, unicode_man_x + 1
    elif what_do_you_do == "MU":
        game_map[unicode_man_y][unicode_man_x] = old_tile
        unicode_man_y, unicode_man_x = unicode_man_y - 1, unicode_man_x
    elif what_do_you_do == "MD":
        game_map[unicode_man_y][unicode_man_x] = old_tile
        unicode_man_y, unicode_man_x = unicode_man_y + 1, unicode_man_x
