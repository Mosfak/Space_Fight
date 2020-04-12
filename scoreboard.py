import pygame.font

class Scoreboard():

	def __init__(self,ai_settings,screen,stats):


		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		self.text_color = (0,255,0)
		self.font = pygame.font.SysFont(None,48)
	
		
