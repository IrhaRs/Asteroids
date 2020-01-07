
import sys
import math
import random
import pygame
from pygame.locals import *
from Objects import Ship,Astroid
from lib import Collision
from res import GameState as gs
import copy

pygame.init()
pygame.font.init()

fps = 30
fpsClock = pygame.time.Clock()
 
width, height = 1000, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Astroids by Irha")

#methods
def newGame():
	global game_state
	global score
	global ship
	global lstAstroids
	game_state=gs.Gamestate.PLAYING
	del lstAstroids[:]
	score=0
	for i in range(7):
		astroidX=random.choice([i for i in range(10,width)if i not in range(math.floor(width/4),math.floor(width-(width/4)))])
		astroidY=random.choice([i for i in range(10,height)if i not in range(math.floor(height/4),math.floor(height-(height/4)))])
		lstAstroids.append(Astroid.Astroid(i,random.randint(1,360),astroidX,astroidY,(random.randint(4,6))))
	ship= Ship.Ship(width//2,height//2)

#variables
game_state = gs.Gamestate.PLAYING
fontGameover = pygame.font.SysFont("Arial",60)
fontScore = pygame.font.SysFont("Arial",30)
textgameover = fontGameover.render('GAME OVER!',True,(255,255,255))
textreset = fontScore.render('Press Space to restart',True,(255,255,255))
textresetRect = textreset.get_rect()
textgameoverRect = textgameover.get_rect()  
# set the center of the rectangular object. 
textgameoverRect.center = (width // 2, height // 2) 
textresetRect.center = (width//2,(height//2)+fontGameover.get_linesize())

ship = Ship.Ship(width//2,height//2)
score = 0
lstAstroids=[]



#start game
newGame()

# Game loop.
while True:
	screen.fill((0, 0, 0))
	keys=pygame.key.get_pressed()
	if game_state==gs.Gamestate.PLAYING:
		if keys[K_UP]:
			ship.move()
		else:
			ship.loseSpeed()
		if keys[K_LEFT]:
			ship.rotate(-5)
		if keys[K_RIGHT]:
			ship.rotate(5)
		if keys[K_RETURN]:
			ship.shoot()
	else:
		if keys[K_SPACE]:
			print("restart game!")
			newGame()
	for event in pygame.event.get():

		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	# Update
	if game_state==gs.Gamestate.PLAYING:
		
		ship.update()
		for i in lstAstroids:
			i.update()
		# Collision
		target = ship
		for astroid in lstAstroids: 
			if(Collision.AABB_Collision_rect(astroid.getAABBShape(10),target.getAABBShape(10))):
				#get circle circle collision between the hitbox of the ship and the astroid
				cx,cy,cr = target.getHitbox()
				if (Collision.Circle_Circle_Collision(astroid.centerpoint[0],astroid.centerpoint[1],astroid.size,cx,cy,cr)):
					#lose
					game_state=gs.Gamestate.GAMEOVER

			for bullet in target.bullets:
				if (Collision.AABB_Collision_rect(astroid.getAABBShape(10),bullet.getAABBShape(10))):
					#check for colision with the astroid and the bullets in radius
					endX,endY = bullet.getEndpoint()
					if (Collision.Circle_Line_Collision(astroid.centerpoint[0],astroid.centerpoint[1],astroid.size,bullet.position[0],bullet.position[1],endX,endY)):
						print("Bullet: "+str(bullet.id)+" hitting astroid: " +str(astroid.id))
						bullet.die()
						score +=10
						if astroid.hit():
							lstAstroids.remove(astroid)
						else:
							#split astroid into two smaller ones
							dup_astroid = copy.deepcopy(astroid)
							dup_astroid.id = dup_astroid.id+500
							astroid.rotate(30)
							dup_astroid.rotate(-30)
							lstAstroids.append(dup_astroid)

	# Draw.
	if game_state==gs.Gamestate.PLAYING:
		textScore = fontScore.render("Score: "+str(score),True,(255,255,255))
		screen.blit(textScore,(20,20))
		ship.draw(screen)
		for i in lstAstroids:
			i.draw(screen)
	elif game_state==gs.Gamestate.GAMEOVER:
		screen.blit(textgameover,textgameoverRect)
		screen.blit(textreset,textresetRect)
		textScore=fontScore.render("Score: "+str(score),True,(255,255,255))
		screen.blit(textScore,(20,20))
	pygame.display.flip()
	fpsClock.tick(fps)