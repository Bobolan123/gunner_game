import pygame
from config import BULLETS_VEL, RED_HIT, WIDTH, YELLOW_HIT


def handle_bullets(yellow_bullets, red_bullets, yellow, red, yellow_gem_absorbed, red_gem_absorbed, increase_vel_bullet):
    for bullet in yellow_bullets:
        if yellow_gem_absorbed:
            bullet.x += increase_vel_bullet
        bullet.x += BULLETS_VEL 

        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        
        if bullet.x >= WIDTH:
            yellow_bullets.remove(bullet)
 
    for bullet in red_bullets:
        if red_gem_absorbed:
            bullet.x -= increase_vel_bullet

        bullet.x -= BULLETS_VEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)

        if bullet.x <=0 - 500:
            red_bullets.remove(bullet)