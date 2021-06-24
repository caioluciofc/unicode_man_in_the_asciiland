class Interactable():

    def __init__(self, y, x, sprite):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.is_used = False

    def health_up(self):
        print("Item was used")
        self.is_used = True
