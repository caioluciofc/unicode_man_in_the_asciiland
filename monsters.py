from math import sqrt


class Monster():

    def __init__(self, health, char, vision_field, monster_y, monster_x, isAgressive=True):
        self.health = health
        self.char = char
        self.vision_field = vision_field
        self.y = monster_y
        self.x = monster_x
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
        self.y = y
        self.x = x
