class Interactable():

    def __init__(self, y, x, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.is_used = False

    def health_up(self, user_health):
        user_health += 20
        self.is_used = True
