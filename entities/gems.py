import pygame
import random
from time import time
from config import BORDER, DECREASE_SPEED, HEIGHT, WIDTH, VEL_DECREASE,GEM_HEIGHT,GEM_WIDTH, BULLETS_VEL

def equal_gems(list_gems):
    random.shuffle(list_gems)
    left = 0
    for i in range(2):
        while list_gems[i].image.x > 600:
            list_gems[i].image.x = random_x()
        list_gems[i].check_collide()
    for i in range(2,4):
        while list_gems[i].image.x < 600:
            list_gems[i].image.x = random_x()  
        list_gems[i].check_collide()

def random_x():
    x = random.randint(0,WIDTH)
    while x > WIDTH//2-5 - GEM_WIDTH and x < WIDTH//2-5 + 10 or x > WIDTH - GEM_WIDTH:
        x = random.randint(0, WIDTH)
    return x 
def random_y():
    y = random.randint(0,WIDTH)  
    while y > HEIGHT - GEM_HEIGHT or y < 100:
        y = random.randint(0,WIDTH)
    return y

class DecreaseSpeedGem(): 
    def __init__(self):
        self.image = pygame.Rect(random_x(),random_y(), GEM_WIDTH, GEM_HEIGHT)
        self.vel_decrease = VEL_DECREASE
        self.check_red_collide = False
        self.check_yellow_collide = False
        
    def check_collide(self): #disapear when entities collide with 
        if self.image.x > BORDER.x:
            self.check_red_collide = True
            self.check_yellow_collide = False
        else:
            self.check_yellow_collide = True
            self.check_red_collide = False

    def handle_gem(self, yellow, red, event):
        if yellow.colliderect(self.image):
            pygame.event.post(pygame.event.Event(event))
            
        if red.colliderect(self.image):
            pygame.event.post(pygame.event.Event(event))


class IncreaseSpeadBullets(DecreaseSpeedGem):
    def __init__(self):
        super().__init__()
        self.bullet_vel = BULLETS_VEL


class Immune(DecreaseSpeedGem):
    def __init__(self):
        super().__init__()


class Lazer(DecreaseSpeedGem):
    pass

#ASSISTANT
class Healing(DecreaseSpeedGem):
    def handle_gem(self, yellow, red, event):
        if yellow.colliderect(self.image):
            pygame.event.post(pygame.event.Event(event))
            self.check_yellow_collide = True
        else:
            self.check_yellow_collide = False
        if red.colliderect(self.image):
            pygame.event.post(pygame.event.Event(event))
            self.check_red_collide = True
        else:
            self.check_red_collide = False
        
class Health_portion(Healing):
    def __init__(self):
        super().__init__()
        self.yellow_side_image = pygame.Rect(0, 300, GEM_WIDTH, GEM_HEIGHT)
        self.red_side_image = pygame.Rect(WIDTH-GEM_WIDTH, 300, GEM_WIDTH, GEM_HEIGHT)
    
    def handle_gem(self, yellow, red, event):
        if yellow.colliderect(self.yellow_side_image):
            pygame.event.post(pygame.event.Event(event))
            self.check_yellow_collide = True
        else:
            self.check_yellow_collide = False
        if red.colliderect(self.red_side_image):
            pygame.event.post(pygame.event.Event(event))
            self.check_red_collide = True
        else:
            self.check_red_collide = False


class Shield_box(Healing):
    def handle_gem(self, yellow, red, event):
        if yellow.colliderect(self.image):
            pygame.event.post(pygame.event.Event(event))
            self.check_yellow_collide = True
        else:
            self.check_yellow_collide = False
        if red.colliderect(self.image):
            pygame.event.post(pygame.event.Event(event))
            self.check_red_collide = True
        else:
            self.check_red_collide = False