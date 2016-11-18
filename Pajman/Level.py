import pygame

class Level:
	def __init__(self, screen, width, height):
		self.width = width
		self.height = height
		self.screen = screen

	def draw(self):
		rect = pygame.draw.rect(self.screen, (255, 0, 255), (0, 0, self.width, self.height))
