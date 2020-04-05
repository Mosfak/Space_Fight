import pygame
import game_functions as gf 
from settings import Settings 
from ship import Ship 
from pygame.sprite import Group


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    screen.fill(ai_settings.bg_color)

    #make a ship
    ship = Ship(ai_settings,screen)
    #Make bullet Group
    bullets = Group()
    
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings,screen,ship,bullets)

        #get rid of bullets off screen
        for bullet in bullets:
            if bullet.rect.bottom < 0:
                bullets.remove(bullet)
        print("live Bullets: ",len(bullets))
    return

run_game()