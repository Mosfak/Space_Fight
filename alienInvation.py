import pygame
import game_functions as gf 
from settings import Settings 
from ship import Ship 
from bullet import Bullet 


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    screen.fill(ai_settings.bg_color)

    #make a ship
    ship = Ship(ai_settings,screen)

    
    while True:
        gf.check_events(ship)
        ship.update()

        gf.update_screen(ai_settings,screen,ship)

        

run_game()