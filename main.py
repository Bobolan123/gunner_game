import pygame
import os
from time import time

from common.utils import background_audio, mix_sound
from config import HEALING, HEALTH_PORTION, HEALTH_RECORVER, IMMUNE ,INCREASE_BULLETS, DECREASE_SPEED, DECREASE_SPEED_GEM, FPS, HEIGHT, INCREASE_VEL_BULLET, LAZER, LAZER_GEM, MAX_BULLET, PROTECT, RED, RED_HIT, RED_SPACESHIP, RED_SPACESHIP_IMAGE, SPACE, SPACESHIP_HEIGHT, SPACESHIP_WIDTH, VEL_DECREASE, WHITE, WIDTH, WIN, BORDER, HEALTH_FONT, WINNER_FONT, YELLOW, YELLOW_HIT, YELLOW_SPACESHIP, GEM_HEIGHT, GEM_WIDTH
from worlds.draw_win import draw_window, draw_winner
from entities.handle_bullet import handle_bullets
from entities.moveable import red_handling_movement, yellow_handling_movement
from entities.spaceship import red_spaceship, yellow_spaceship
from entities.gems import DecreaseSpeedGem, Healing, Health_portion, IncreaseSpeadBullets, Immune, Lazer, Shield_box, equal_gems
pygame.font.init()



def main():
    background_audio('background_sound.wav')    
    BULLET_FIRE_SOUND = mix_sound('Gun+Silencer.mp3')
    BULLET_HIT_SOUND = mix_sound('Grenade+1.mp3')

    yellow = yellow_spaceship()
    red = red_spaceship()

    #GEM
    decrease_speed_gem = DecreaseSpeedGem()
    disapear_decrease_speed_gem = False
    vel_decrease = 0
    decrease_speed_gem.check_collide() #check yellow_absorb = True or red_absorb = True and vice verses

    increase_bullet_gem = IncreaseSpeadBullets()
    increase_vel_bullet = 0
    disapear_increase_bullet_gem = False
    increase_bullet_gem.check_collide() 

    immune_gem = Immune()
    immune_gem.check_collide()
    disapear_immune_gem = False
    immune_power = False
    start_immune_time = 0 #tackle error before entity collide with immune_gem

    lazer = Lazer()
    lazer.check_collide()
    disapear_lazer_gem = False
    lazer_bullets_check = False

    equal_gems([decrease_speed_gem, increase_bullet_gem, immune_gem, lazer])

    #ASSISTANT
    heal = Healing()
    heal.check_collide()
    disapear_heal = False

    health_portion = Health_portion()
    health_portion.check_collide()
    last_health_increase_time = pygame.time.get_ticks()

    shield_box = Shield_box()
    shield_box.check_collide()
    disapear_shield_box = False
    yellow_shield = False
    red_shield = False
    last_shield_box = pygame.time.get_ticks()

    clock = pygame.time.Clock()
    run = True
    start_game = time()
    

    while run:
        clock.tick(FPS)

        if time()-start_game > 5: #used to check time to appear new healing_box each 5 seconds
            heal = Healing()
            start_game = time()
            disapear_heal = False
        
        dt = (pygame.time.get_ticks() - last_health_increase_time) /1000.0 #delta time to handle health_portion active each 2s
        
        dt_shield_box = (pygame.time.get_ticks() - last_shield_box) /1000.0
        if dt_shield_box > 3:
            shield_box = Shield_box()
            last_shield_box = pygame.time.get_ticks()
            disapear_shield_box = False

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                
                run = False
                pygame.quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow.bullets) < MAX_BULLET:
                    if lazer_bullets_check and lazer.check_yellow_collide:
                        bullet = pygame.Rect(
                        yellow.yellow.x + yellow.yellow.width, yellow.yellow.y + yellow.yellow.height//2-2, 500, 10)
                    else:
                        bullet = pygame.Rect(
                        yellow.yellow.x + yellow.yellow.width, yellow.yellow.y + yellow.yellow.height//2-2, 10, 5)
                    yellow.bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red.bullets) < MAX_BULLET:
                    if lazer_bullets_check and lazer.check_red_collide:
                        bullet = pygame.Rect(
                        red.red.x - 500, red.red.y + red.red.height//2-2, 500, 10)
                    else:
                        bullet = pygame.Rect(
                        red.red.x, red.red.y + red.red.height//2-2, 10, 5)
                    red.bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == DECREASE_SPEED:
                disapear_decrease_speed_gem = True
                vel_decrease = VEL_DECREASE
                
            if event.type == INCREASE_BULLETS:
                disapear_increase_bullet_gem = True
                increase_vel_bullet = INCREASE_VEL_BULLET

            if event.type == IMMUNE:
                start_immune_time = time()
                disapear_immune_gem = True
                immune_power = True
                
            if event.type == LAZER:
                disapear_lazer_gem = True
                lazer_bullets_check = True

            #ASSISTANT
            if event.type == HEALING:
                disapear_heal = True
                if heal.check_yellow_collide:
                    yellow.health =10 
                if heal.check_red_collide:
                    red.health = 10

            if event.type == HEALTH_RECORVER:
                if dt >= 2.0:
                    if health_portion.check_yellow_collide and yellow.health <10:
                        yellow.health += 1
                    if health_portion.check_red_collide and red.health < 10:
                        red.health += 1
                    last_health_increase_time = pygame.time.get_ticks()

            if event.type == PROTECT:
                disapear_shield_box = True
                if shield_box.check_yellow_collide:
                    yellow_shield = True
                if shield_box.check_red_collide:
                    red_shield = True

            if event.type == YELLOW_HIT:
                if yellow_shield:
                    yellow.health +=1
                yellow_shield = False

                end = time() - start_immune_time
                if immune_power and immune_gem.check_yellow_collide and round(end) < 5:
                    yellow.health +=1
                yellow.health -=1
                if decrease_speed_gem.check_red_collide:
                    yellow.yellow.x -= vel_decrease
                    if yellow.yellow.x < 0:
                        yellow.yellow.x +=vel_decrease 
                BULLET_HIT_SOUND.play()

            if event.type == RED_HIT:
                if red_shield:
                    red.health +=1
                red_shield = False

                end = time() - start_immune_time 
                if immune_power and immune_gem.check_red_collide and round(end) < 5:
                    red.health +=1
                red.health -=1
                if decrease_speed_gem.check_yellow_collide:
                    red.red.x += vel_decrease
                    if red.red.x > WIDTH - GEM_WIDTH:
                        red.red.x -= vel_decrease
                BULLET_HIT_SOUND.play()

                

        winner_text = ""
        if yellow.health <=0:
            winner_text = "RED WINS"
        if red.health <=0:
            winner_text = "YELLOW WINS"
        if winner_text != "":
            draw_window(yellow.yellow, red.red, yellow.bullets, red.bullets, yellow.health, red.health, 
                    disapear_decrease_speed_gem, decrease_speed_gem.image, 
                    disapear_increase_bullet_gem, increase_bullet_gem.image, 
                    disapear_immune_gem, immune_gem.image,
                    disapear_lazer_gem, lazer.image,
                    disapear_heal, heal.image,
                    health_portion.yellow_side_image, health_portion.red_side_image,
                    disapear_shield_box, shield_box.image ,yellow_shield, red_shield)            
            draw_winner(winner_text)
            break
        
        
        key_pressed = pygame.key.get_pressed()
        yellow_handling_movement(key_pressed, yellow.yellow) 
        red_handling_movement(key_pressed, red.red)        
        handle_bullets(yellow.bullets, red.bullets, yellow.yellow, red.red, 
            increase_bullet_gem.check_yellow_collide, increase_bullet_gem.check_red_collide, increase_vel_bullet) 
        #is rect: yellow.yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
        
        decrease_speed_gem.handle_gem(yellow.yellow, red.red, DECREASE_SPEED)
        increase_bullet_gem.handle_gem(yellow.yellow, red.red, INCREASE_BULLETS)
        immune_gem.handle_gem(yellow.yellow, red.red, IMMUNE)
        lazer.handle_gem(yellow.yellow, red.red, LAZER)
        heal.handle_gem(yellow.yellow, red.red, HEALING)
        health_portion.handle_gem(yellow.yellow, red.red, HEALTH_RECORVER)
        shield_box.handle_gem(yellow.yellow, red.red, PROTECT)

        draw_window(yellow.yellow, red.red, yellow.bullets, red.bullets, yellow.health, red.health, 
                    disapear_decrease_speed_gem, decrease_speed_gem.image, 
                    disapear_increase_bullet_gem, increase_bullet_gem.image, 
                    disapear_immune_gem, immune_gem.image,
                    disapear_lazer_gem, lazer.image,
                    disapear_heal, heal.image,
                    health_portion.yellow_side_image, health_portion.red_side_image,
                    disapear_shield_box, shield_box.image ,yellow_shield, red_shield)
        
    
    main()

if __name__ == "__main__":
    main()