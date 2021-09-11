import pygame


# =============== Main Classes ==================== #
# This class represent the main character. IDK what is going to be

class Character:




# This class represent the battle arena.
class BattleRectangle:
    def __init__(self, character, actions):
        self.character = character
        self.actions = actions

    def appears(self):
        pass


# This represent the actions made up on the game.
class Actions:
    def __init__(self, key):
        self.key = key


# ==================BASE GAME==================== #
pygame.init()
screen = pygame.display.set_mode((800, 600))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# ==================BASE GAME==================== #
