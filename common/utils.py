
import pygame
import os

pygame.mixer.init()

def load_assistant_image(file):
    return pygame.image.load(os.path.join('Assets','assistant',file))

def load_gem_image(file):
    return pygame.image.load(os.path.join('Assets','gems',file))
                             
def load_spaceship_image(file):
    return pygame.image.load(os.path.join('Assets', file))

def scale_gem_image(image, width, height):
    return pygame.transform.scale(image,(width, height))

def scale_spaceship_image(image, rolate, width, height):
    return pygame.transform.scale(
    pygame.transform.rotate(image, rolate), (width, height))

#SOUND
def mix_sound(file):
    return pygame.mixer.Sound(os.path.join('Assets', file))

def background_audio(file):
    pygame.mixer.music.load(os.path.join('Assets', 'sound', file))
    pygame.mixer.music.play()