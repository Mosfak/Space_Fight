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


def get_number_rows(ai_settings,ship_height,alien_height):
	#subtracted 3 aliens because we need 3 row empty from the bottom
	available_space_y = (ai_settings.screen_height - 6 * alien_height - ship_height)
	#each alien needs some extra space avobe and below it
	num_rows = int(available_space_y / (2*alien_height))
	return num_rows

def get_number_aliens(ai_settings,screen,aliens):
	alien = Alien(ai_settings,screen)
	available_space_x = ai_settings.screen_width - 2* alien.width 
	number_aliens_x = int(available_space_x / (2* alien.width)) 
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
		alien = Alien(ai_settings,screen)
		alien.x = alien.width +2 * alien.width * alien_number
		alien.rect.x = alien.x
		#one alien empty space...and for each alien we need space of two 
		#and to have rect we need to multiply with row number
		alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
		aliens.add(alien)


def create_fleet(ai_settings,screen,ship, aliens):
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens(ai_settings,screen,aliens)
	num_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	for row_number in range(num_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)


def update_bullets(aliens,bullets):
	for bullet in bullets:
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
	#check collitions
	collitions = pygame.sprite.groupcollide(bullets,aliens,True,True)



def update_screen(ai_settings,screen,ship,aliens,bullets,stars):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	stars.draw(screen)
	#little confusion
	#why bullets.sprites() while bullet just works fine--------?
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	pygame.display.flip()

