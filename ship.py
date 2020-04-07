import pygame

class Ship():


	def __init__(self,ai_settings,screen):
		self.screen = screen
		self.ai_settings = ai_settings
		#load image of the ship
		self.image = pygame.image.load("images/ship.png")
		self.image= pygame.transform.rotozoom(self.image, 0, 0.3)
		self.rect = self.image.get_rect()
		self.screen_rect  =  screen.get_rect()
		#start each ship at the bottom center
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom

		#movement flag
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		#decimal value for ship center
		self.center = float(self.rect.centerx)
		self.centery = float(self.rect.centery)

		#ship speed
		self.speed = self.ai_settings.ship_speed_factor


	def blitme(self):
		"""draw the ship at its current location"""

		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right and self.rect.right<self.screen_rect.right:
			self.center+=self.speed
		if self.moving_left and self.rect.left>self.screen_rect.left:
			self.center-=self.speed
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.centery-=self.speed
		if self.moving_down and self.rect.bottom <self.screen_rect.bottom:
			self.centery+=self.speed

		#update ship center
		self.rect.centerx = self.center
		self.rect.centery = self.centery