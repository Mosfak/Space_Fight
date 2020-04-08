import pygame
import game_functions as gf 
from settings import Settings 
from ship import Ship 
from pygame.sprite import Group
from alien import Alien
import random
from star import Star

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Space Fight")
    screen.fill(ai_settings.bg_color)

    #make a ship
    ship = Ship(ai_settings,screen)
    #Make bullet Group
    bullets = Group()
    
    #Make alien group
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship, aliens)

    #Make star group
    stars = Group()
    star_number = 100
    for i in range(star_number):
        stars.add(Star(screen))

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_bullets(aliens,bullets)
        gf.alien_update(aliens)
        stars.update()
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,stars)
        
        
        #print("live Bullets: ",len(bullets))
    return

run_game()
