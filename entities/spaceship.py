import pygame

from config import HEALTH, SPACESHIP_HEIGHT, SPACESHIP_WIDTH, WIDTH



class yellow_spaceship:
    def __init__(self):
        self.yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  
        self.health = HEALTH
        self.bullets = []

class red_spaceship:
    def __init__(self):
        self.red = pygame.Rect(WIDTH-SPACESHIP_WIDTH - 100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)  
        self.health = HEALTH
        self.bullets = []