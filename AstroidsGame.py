
import sys
 
import pygame
from pygame.locals import *
from Objects import Ship

pygame.init()
 
fps = 30
fpsClock = pygame.time.Clock()
 
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Astroids by Irha")

ship = Ship.Ship()
 
# Game loop.
while True:
	screen.fill((0, 0, 0))
	keys=pygame.key.get_pressed()
	if keys[K_UP]:
		ship.move()
	else:
		ship.loseSpeed()
	if keys[K_LEFT]:
		ship.rotate(-5)
	if keys[K_RIGHT]:
		ship.rotate(5)
	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# Update
	ship.update()
	# Draw.
	ship.draw(screen)

	pygame.display.flip()
	fpsClock.tick(fps)