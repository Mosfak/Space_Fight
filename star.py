import pygame as pg 
import random
from pygame.sprite import Sprite

class Star(Sprite):

	def __init__(self,screen):
		super().__init__()
		self.screen = screen
		#self.ai_settings = ai_settings
		self.image = pg.image.load("images/star.png")
		self.image = pg.transform.rotozoom(self.image,0,random.uniform(0.01,0.02))
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		self.rect.centerx = random.randint(0,self.screen_rect.right)
		self.rect.centery = random.randint(0,self.screen_rect.bottom)

	def blitme(self):
		self.screen.blit(self.image,self.rect)

