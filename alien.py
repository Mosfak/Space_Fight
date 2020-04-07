import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	"A class to represent a single alien"

	def __init__(self,ai_settings,screen):

		super(Alien,self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#load the image of alien image
		self.image = pygame.image.load("images/alien.png")
		self.image = pygame.transform.rotozoom(self.image,0,0.07)
		self.rect = self.image.get_rect()

		#its dimension
		self.width = self.rect.width
		self.height = self.rect.height

		#start the alien at top of the screen

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store the aliens exact position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def blitme(self):
		self.screen.blit(self.image,self.rect)