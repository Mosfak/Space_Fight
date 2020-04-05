import sys
import pygame
from bullet import Bullet

def check_keypress(event,ai_settings,screen,ship,bullets):
	"""Response to key press"""
	if event.key == pygame.K_RIGHT:
		#move the ship to right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left =True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		bullet.fire = True


def check_keyrelease(event,ship):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left =False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False
	

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
        	check_keypress(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
        	check_keyrelease(event,ship)

        
def update_screen(ai_settings,screen,ship,bullets):
	screen.fill(ai_settings.bg_color)
	ship.blitme()

	#little confusion
	#why bullets.sprites() while bullet just works fine--------?
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()
