import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
	screen_rect = screen.get_rect()
	for alien in aliens:
		if(alien.rect.bottom >= screen_rect.bottom):
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
			break

def is_game_over(ai_settings,screen,stats,ship,aliens,bullets):
	if(stats.ship_left<=0):
		stats.reset_stats()
		aliens.empty()
		bullets.empty()
		create_fleet(ai_settings,screen, ship , aliens)
		ship.restart()


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	if stats.ship_left > 0:

		#decrement of ships left
		stats.ship_left -= 1

		#empty aliens and bullets
		aliens.empty()
		bullets.empty()

		#create new fleet of aliens and recenter ship
		create_fleet(ai_settings,screen,ship, aliens)
		ship.restart()
		#pause
		sleep(0.5)
	else:
		stats.game_active = False
		ai_settings.initialize_dynamic_settings()


def check_keypress(event,ai_settings,screen,stats,ship,bullets,aliens):
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
		if not stats.game_active:
			stats.game_active =True
		elif len(bullets)< ai_settings.bullets_allowed or ai_settings.bullets_limited == False:
			bullets.add(Bullet(ai_settings,screen,ship))
	elif event.key == pygame.K_q:
		sys.exit()
	elif event.key == pygame.K_p:
		#print(stats.ship_left)
		#is_game_over(ai_settings,screen,stats,ship,aliens,bullets)
		if(stats.ship_left<=0):
			stats.reset_stats()
			aliens.empty()
			bullets.empty()
			create_fleet(ai_settings,screen, ship , aliens)
			ship.restart()
		stats.game_active = not stats.game_active
	elif event.key == pygame.K_ESCAPE:
		#is_game_over(ai_settings,stats,screen,ship,aliens,bullets)
		if(stats.ship_left<=0):
			stats.reset_stats()
			aliens.empty()
			bullets.empty()
			create_fleet(ai_settings,screen, ship , aliens)
			ship.restart()
		stats.game_active = False



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


def check_play_button(ai_settings,screen,ship,aliens,bullets,stats,play_button,mousex,mousey):
	if play_button.rect.collidepoint(mousex,mousey):
		is_game_over(ai_settings,screen,stats,ship,aliens,bullets)
		stats.game_active = True


def check_events(ai_settings,screen,stats,play_button,ship,bullets,aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type ==pygame.MOUSEBUTTONDOWN:
        	mousex,mousey = pygame.mouse.get_pos()
        	check_play_button(ai_settings,screen,ship,aliens,bullets,stats,play_button,mousex,mousey)
        elif event.type == pygame.KEYDOWN:
        	check_keypress(event,ai_settings,screen,stats,ship,bullets,aliens)
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

def drop_aliens(aliens):
	for alien in aliens:
		alien.rect.y+=alien.ai_settings.alien_drop_speed

def alien_update(ai_settings,stats,screen,ship,aliens,bullets):
	#left right moving functionality
	for alien in aliens:
		if(alien.rect.right>= alien.screen_rect.right):
			alien.ai_settings.alien_direction = -1
			drop_aliens(aliens)
		elif alien.rect.left <=0:
			alien.ai_settings.alien_direction = 1
			drop_aliens(aliens)
		alien.rect.x+=(alien.ai_settings.alien_speed * alien.ai_settings.alien_direction)
	
	#looking for alien reaching bottom
	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)

	#Looking for alien -ship crash
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)

def check_collitions(ai_settings,screen,ship,aliens,bullets):
	collitions = pygame.sprite.groupcollide(bullets,aliens,True,True)
	if len(aliens) == 0:
		#vanish all the bullets
		bullets.remove()
		#speed up the game 
		ai_settings.increase_speed()
		#recreate the alien fleet
		create_fleet(ai_settings,screen,ship, aliens)
	return collitions 


def update_bullets(ai_settings,screen,ship,aliens,bullets):
	for bullet in bullets:
		if bullet.rect.bottom < 0:
			bullets.remove(bullet)
	#check collitions
	check_collitions(ai_settings,screen,ship,aliens,bullets)
	



def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,stars,play_button):
	screen.fill(ai_settings.bg_color)
	ship.blitme()
	aliens.draw(screen)
	stars.draw(screen)
	sb.show_score()
	#little confusion
	#why bullets.sprites() while bullet just works fine--------?
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	if not stats.game_active:
		play_button.draw_button()
	pygame.display.flip()

