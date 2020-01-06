
import sys

import random
import pygame
from pygame.locals import *
from Objects import Ship,Astroid
from lib import Collision
import copy

pygame.init()
 
fps = 30
fpsClock = pygame.time.Clock()
 
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Astroids by Irha")

ship = Ship.Ship()
lstAstroids=[]
for i in range(7):
	lstAstroids.append(Astroid.Astroid(i,random.randint(1,360),random.randint(100, 900),random.randint(100,600),(random.randint(4,6))))

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
	# Collision
	target = ship
	for astroid in lstAstroids: 
		if(Collision.AABB_Collision_rect(astroid.getAABBShape(10),target.getAABBShape(10))):
			print("astroid "+str(astroid.id)+" hitting target ")
		for bullet in target.bullets:
			if (Collision.AABB_Collision_rect(astroid.getAABBShape(10),bullet.getAABBShape(10))):
				#check for colision with the astroid and the bullets in radius
				endX,endY = bullet.getEndpoint()
				if (Collision.Circle_Line_Collision(astroid.centerpoint[0],astroid.centerpoint[1],astroid.size,bullet.position[0],bullet.position[1],endX,endY)):
					print("Bullet: "+str(bullet.id)+" hitting astroid: " +str(astroid.id))
					bullet.die()
					if astroid.hit():
						lstAstroids.remove(astroid)
					else:
						dup_astroid = copy.deepcopy(astroid)
						dup_astroid.id = dup_astroid.id+500
						astroid.rotate(30)
						dup_astroid.rotate(-30)
						lstAstroids.append(dup_astroid)

	# Draw.
	ship.draw(screen)
	for i in lstAstroids:
		i.draw(screen)

	pygame.display.flip()
	fpsClock.tick(fps)