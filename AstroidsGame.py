
import sys

import random
import pygame
from pygame.locals import *
from Objects import Ship,Astroid

pygame.init()
 
fps = 30
fpsClock = pygame.time.Clock()
 
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Astroids by Irha")

ship = Ship.Ship()
lstAstroids=[]
for i in range(7):
	lstAstroids.append(Astroid.Astroid(random.randint(1,360),random.randint(100, 900),random.randint(100,600),(random.randint(4,6)*10)))

# Game loop.
while True:
	screen.fill((0, 0, 0))
	keys=pygame.key.get_pressed()
	if keys[K_UP]:
		ship.move()
	else:
		ship.loseSpeed()
	if keys[K_LEFT]:
		ship.rotate(-8)
	if keys[K_RIGHT]:
		ship.rotate(8)
	if keys[K_TAB]:
		ship.shoot()
	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# Update
	ship.update()
	for i in lstAstroids:
		i.update()
	# Draw.
	ship.draw(screen)
	for i in lstAstroids:
		i.draw(screen)

	pygame.display.flip()
	fpsClock.tick(fps)