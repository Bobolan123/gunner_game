import pygame

from config import BORDER, HEIGHT, SPACESHIP_HEIGHT, SPACESHIP_WIDTH, VEL, WIDTH


def yellow_handling_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a] and yellow.x >=0 : #left
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + SPACESHIP_WIDTH <= BORDER.x: #right
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y >= 0: #up
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + SPACESHIP_HEIGHT <= HEIGHT: #down
        yellow.y += VEL

def red_handling_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT] and red.x >= BORDER.x + BORDER.width: #left
        red.x -= VEL 
    if key_pressed[pygame.K_RIGHT] and red.x + SPACESHIP_WIDTH <= WIDTH: #right
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y >= 0: #up
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y + SPACESHIP_HEIGHT <= HEIGHT: #down
        red.y += VEL