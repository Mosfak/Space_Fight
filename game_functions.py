import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_keypress(event,ai_settings,screen,ship,bullets):
	"""Response to key press"""
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		#move the ship to right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left =True
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		if len(bullets)< ai_settings.bullets_allowed or ai_settings.bullets_limited == False:
			bullets.add(Bullet(ai_settings,screen,ship))
	elif event.key == pygame.K_q:
		sys.exit()



def check_keyrelease(event,ship):
	"""Respond to key releases."""
	if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
		ship.moving_left =False
	elif event.key == pygame.K_UP or event.key == pygame.K_w:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
		ship.moving_down = False
	

def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
        	check_keypress(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
        	check_keyrelease(event,ship)


def get_number_aliens(ai_settings,screen,aliens):
	alien = Alien(ai_settings,screen)
	available_space_x = ai_settings.screen_width - 2* alien.width 
	number_aliens_x = int(available_space_x / (2* alien.width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number):
		alien = Alien(ai_settings,screen)
		alien.x = alien.width +2 * alien.width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)


def create_fleet(ai_settings,screen, aliens):
	number_aliens_x = get_number_aliens(ai_settings,screen,aliens)
	for alien_number in range(number_aliens_x):
		create_alien(ai_settings,screen,aliens,alien_number)

def update_screen(ai_settings,screen,ship,aliens,bullets):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	#little confusion
	#why bullets.sprites() while bullet just works fine--------?
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()
