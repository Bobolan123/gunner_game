import pygame
from common.utils import background_audio
from config import LOADING_FONT, HEALING_BOX, HEALTH_PORTION, IMMUNE_GEM, INCREASE_BULLETS_GEM, BORDER, GEM_HEIGHT, GEM_WIDTH, HEALTH_FONT, HEIGHT, LAZER_GEM, RED, RED_SHIELD, RED_SPACESHIP, SHIELD_BOX, SPACE, WHITE, WIDTH, WIN, WINNER_FONT, YELLOW, YELLOW_SHIELD, YELLOW_SPACESHIP, DECREASE_SPEED_GEM, INSIDE_LOADING_WIDTH
from worlds.loading import Loading

def draw_window(yellow, red, yellow_bullets, red_bullets, yellow_health, red_health, 
                disapear_decrease_speed_gem, decrease_speed_gem, disapear_increase_bullet_gem, 
                increase_bullet_gem, disapear_immune_gem, immune_gem,
                disapear_lazer_gem, lazer_gem, 
                disapear_heal, heal_box,
                yellow_side_health_portion, red_side_health_portion,
                disapear_shield_box, shield_box, yellow_shield, red_shield):
    WIN.blit(SPACE,(0,0))
    pygame.draw.rect(WIN, WHITE, BORDER)
    
    #GEM
    if not disapear_decrease_speed_gem:
        WIN.blit(DECREASE_SPEED_GEM, (decrease_speed_gem.x, decrease_speed_gem.y)) #GEM
    if not disapear_increase_bullet_gem:
        WIN.blit(INCREASE_BULLETS_GEM, (increase_bullet_gem.x, increase_bullet_gem.y)) #GEM
    if not disapear_immune_gem:
        WIN.blit(IMMUNE_GEM, (immune_gem.x, immune_gem.y))
    if not disapear_lazer_gem:
        WIN.blit(LAZER_GEM, (lazer_gem.x, lazer_gem.y))
    if not disapear_heal:
        WIN.blit(HEALING_BOX, (heal_box.x, heal_box.y))
    if not disapear_shield_box:
        WIN.blit(SHIELD_BOX, (shield_box.x, shield_box.y))

    #DRAW 2 HEALTH PORTION
    WIN.blit(HEALTH_PORTION, (yellow_side_health_portion.x, yellow_side_health_portion.y))
    WIN.blit(HEALTH_PORTION, (red_side_health_portion.x, red_side_health_portion.y))
    
   
    red_health_text = HEALTH_FONT.render("Health: " + str(red_health),1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health),1, WHITE)
    
    #2 SPACESHIP AND HEALTH       
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width(), 10))
    WIN.blit(yellow_health_text, (10, 10))
    
    if yellow_shield:
        WIN.blit(YELLOW_SHIELD, (yellow.x, yellow.y))    
    else:
        WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
   
    if red_shield:
        WIN.blit(RED_SHIELD, (red.x, red.y))    
    else:
        WIN.blit(RED_SPACESHIP, (red.x, red.y))


    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.display.update() 


loading = Loading()
text_loading = LOADING_FONT.render("LOADING...", True, RED)
def draw_winner(winner_text):
    #DRAW WINNING
    if "YELLOW" in winner_text:
        draw_text = WINNER_FONT.render(winner_text, 1, (255, 255, 150))
    else:
        draw_text = WINNER_FONT.render(winner_text, 1, (242, 77, 77))

    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width() /2,
                          HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    background_audio('victory.wav')
    pygame.time.delay(2000)
    
    #DRAWLOADING
    for i in range(10):
        handle_inside_loading(100) #delay 10 times to draw inside_loading from 0 -> 780
    loading.inside_loading.width = 0


def draw_loading(inside_loading, outside_loading):
    pygame.draw.rect(WIN, RED, outside_loading, 2)
    pygame.draw.rect(WIN, RED, inside_loading)

def handle_inside_loading(time):
    pygame.draw.rect(WIN, (0,0,0), pygame.Rect(0,0,WIDTH,HEIGHT))

    WIN.blit(text_loading, (WIDTH/2 - text_loading.get_width()/2, 10))

    loading.inside_loading.width += 78
    draw_loading(loading.inside_loading, loading.outside_loading)
    pygame.display.flip()
    pygame.time.delay(time)
