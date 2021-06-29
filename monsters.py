from math import sqrt
import random


class Monster():

    def __init__(self, health, char, vision_field, monster_y, monster_x, strength=1, defense=1, isAgressive=True):
        self.health = health
        self.char = char
        self.vision_field = vision_field
        self.y = monster_y
        self.x = monster_x
        self.strength = strength
        self.defense = defense
        self.isAgressive = isAgressive

    def calculate_path(self, player_y, player_x):
        distance_monster_player = sqrt(
            (player_x - self.x) ** 2 + (player_y - self.y) ** 2)
        if distance_monster_player <= self.vision_field:
            option1 = sqrt((player_x - (self.x - 1)) **
                           2 + (player_y - self.y) ** 2)
            option2 = sqrt((player_x - (self.x + 1)) **
                           2 + (player_y - self.y) ** 2)
            option3 = sqrt((player_x - self.x) ** 2 +
                           (player_y - (self.y - 1)) ** 2)
            option4 = sqrt((player_x - self.x) ** 2 +
                           (player_y - (self.y + 1)) ** 2)
            options = [option1, option2, option3, option4]
            sorted_options = sorted(options)
            if sorted_options[0] == option1:
                return [self.y, self.x - 1]
            elif sorted_options[0] == option2:
                return [self.y, self.x + 1]
            elif sorted_options[0] == option3:
                return [self.y - 1, self.x]
            elif sorted_options[0] == option4:
                return [self.y + 1, self.x]
        return [self.y, self.x]

    def walk_to_player(self, y, x):
        d6_roll = random.randint(1, 7)
        if d6_roll >= 3:
            self.y = y
            self.x = x

    def attack_player(self, player_def):
        d6_roll = random.randint(1, 7)
        damage = ((d6_roll * self.strength)/2)-player_def
        if damage <= 0:
            return 0
        return damage

    def monster_action(self, player_x, player_y, player_def):
        distance_monster_player = sqrt(
            (player_x - self.x) ** 2 + (player_y - self.y) ** 2)
        if distance_monster_player < 2:
            self.attack_player(player_def)
        elif distance_monster_player < self.vision_field:
            self.walk_to_player()
