import pygame as pg

class Button:

	def __init__(self,ai_settings,screen,msg):
		self.ai_settings = ai_settings
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#dimension
		self.width = 200
		self.height = 50


		#position
		self.rect = pg.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center


		#properties
		self.button_color = (0, 255,0)
		self.text_color = (255,255,255)
		self.font = pg.font.SysFont(None,48)

		#msg handling
		self.msg_prep(msg)

	def msg_prep(self,msg):

		self.msg_img = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_img_rect = self.msg_img.get_rect()
		self.msg_img_rect.center = self.rect.center

	def draw_button(self):
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_img,self.msg_img_rect)