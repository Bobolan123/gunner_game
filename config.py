import os
import pygame
from common.utils import load_assistant_image, load_gem_image, load_spaceship_image, scale_gem_image, scale_spaceship_image
pygame.font.init()
pygame.mixer.init()

#WIN
WIDTH, HEIGHT = 1200, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gunner")
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

#BORDER
BORDER = pygame.Rect(WIDTH//2-5, 0, 10, HEIGHT)

#BACKGROUND
SPACE = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets','space.png')), (WIDTH, HEIGHT)
)

FPS = 60

#SPACESHIP_INFORMATION
VEL = 5
BULLETS_VEL = 7
MAX_BULLET = 100
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 40

YELLOW_HIT = pygame.USEREVENT + 1 
RED_HIT = pygame.USEREVENT + 2

#CHARACTERS
YELLOW_SPACESHIP_IMAGE = load_spaceship_image('spaceship_yellow.png')
YELLOW_SPACESHIP = scale_spaceship_image(YELLOW_SPACESHIP_IMAGE,90, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

RED_SPACESHIP_IMAGE = load_spaceship_image('spaceship_red.png')
RED_SPACESHIP = scale_spaceship_image(RED_SPACESHIP_IMAGE, -90, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

#HEALTH
HEALTH = 10
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100, bold=True)


#GEM
GEM_WIDTH = 40
GEM_HEIGHT = 40

VEL_DECREASE = 50
DECREASE_SPEED = pygame.USEREVENT+10
DECREASE_SPEED_IMMAGE = load_gem_image('decrease_speed.png')
DECREASE_SPEED_GEM = scale_gem_image(DECREASE_SPEED_IMMAGE, GEM_WIDTH, GEM_HEIGHT)


IMMUNE = pygame.USEREVENT+11
IMMUNE_IMMAGE = load_gem_image('immune.png')
IMMUNE_GEM = scale_gem_image(IMMUNE_IMMAGE, GEM_WIDTH, GEM_HEIGHT)

INCREASE_VEL_BULLET = 30
INCREASE_BULLETS = pygame.USEREVENT+12
INCREASE_BULLETS_IMAGE = load_gem_image('increase_bullets.png')
INCREASE_BULLETS_GEM= scale_gem_image(INCREASE_BULLETS_IMAGE, GEM_WIDTH, GEM_HEIGHT)

LAZER = pygame.USEREVENT+13
LAZER_IMAGE = load_gem_image('lazer.png')
LAZER_GEM = scale_gem_image(LAZER_IMAGE, GEM_WIDTH, GEM_HEIGHT)

#ASSISTANT
HEALING = pygame.USEREVENT+20
HEALING_IMAGE = load_assistant_image('heal_box.png')
HEALING_BOX = scale_gem_image(HEALING_IMAGE, GEM_WIDTH, GEM_HEIGHT)

HEALTH_RECORVER = pygame.USEREVENT+21
HEALTH_PORTION_IMAGE = load_assistant_image('health_portion.png')
HEALTH_PORTION = scale_gem_image(HEALTH_PORTION_IMAGE, GEM_WIDTH, GEM_HEIGHT)


PROTECT = pygame.USEREVENT+22
SHIELD_BOX_IMAGE = load_assistant_image('shield_box.png')
SHIELD_BOX = scale_gem_image(SHIELD_BOX_IMAGE, GEM_WIDTH, GEM_HEIGHT)

SHIELD_IMAGE = load_assistant_image('shield.png')
SHIELD = scale_gem_image(SHIELD_IMAGE, GEM_WIDTH, GEM_HEIGHT)

YELLOW_SHIELD_IMAGE = load_spaceship_image('yellow_shield.png')
YELLOW_SHIELD = scale_spaceship_image(YELLOW_SHIELD_IMAGE, 90, GEM_WIDTH, GEM_HEIGHT)
RED_SHIELD_IMAGE = load_spaceship_image('red_shield.png')
RED_SHIELD = scale_spaceship_image(RED_SHIELD_IMAGE, -90, GEM_WIDTH, GEM_HEIGHT)


#LOADING
LOADING_WIDTH = 800
LOADING_HEIGHT = 200
INSIDE_LOADING_WIDTH = 0
LOADING_FONT = pygame.font.SysFont('comicsans', 100, bold=True)
