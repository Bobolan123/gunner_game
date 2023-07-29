import pygame
from config import HEIGHT, WIDTH, LOADING_WIDTH,LOADING_HEIGHT, INSIDE_LOADING_WIDTH


class Loading():
    def __init__(self):
        self.outside_loading = pygame.Rect((WIDTH-LOADING_WIDTH)/2, (HEIGHT-LOADING_HEIGHT)/2, LOADING_WIDTH, LOADING_HEIGHT)
        self.inside_loading = pygame.Rect((WIDTH-LOADING_WIDTH)/2+10, (HEIGHT-LOADING_HEIGHT)/2 +10, INSIDE_LOADING_WIDTH, LOADING_HEIGHT-20)


        