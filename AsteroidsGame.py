
import sys
import math
import random
import pygame
from pygame.locals import *
from Objects import Ship,Asteroid
from lib import Collision
from res import GameState as gs
import copy
import Settings as s

pygame.init()
pygame.font.init()

fps = 30
fpsClock = pygame.time.Clock()
 
width, height = s.WIDTH, s.HEIGHT
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Asteroids by Irha")

#methods
def newGame():
	global game_state
	global score
	global ship
	global lstasteroids
	game_state=gs.Gamestate.PLAYING
	del lstasteroids[:]
	score=0
	for i in range(7):
		asteroidX=random.choice([i for i in range(10,width)if i not in range(math.floor(width/4),math.floor(width-(width/4)))])
		asteroidY=random.choice([i for i in range(10,height)if i not in range(math.floor(height/4),math.floor(height-(height/4)))])
		lstasteroids.append(Asteroid.Asteroid(i,random.randint(1,360),asteroidX,asteroidY,(random.randint(4,6))))
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
lstasteroids=[]



#start game
newGame()

# Game loop.
while True:
	screen.fill((0, 0, 0))
	keys=pygame.key.get_pressed()
	if game_state==gs.Gamestate.PLAYING:
		if keys[s.FORWARD]:
			ship.move()
		else:
			ship.loseSpeed()
		if keys[s.LEFT]:
			ship.rotate(-5)
		if keys[s.RIGHT]:
			ship.rotate(5)
		if keys[s.SHOOT]:
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
		for i in lstasteroids:
			i.update()
		# Collision
		target = ship
		for asteroid in lstasteroids: 
			if(Collision.AABB_Collision_rect(asteroid.getAABBShape(10),target.getAABBShape(10))):
				#get circle circle collision between the hitbox of the ship and the asteroid
				cx,cy,cr = target.getHitbox()
				if (Collision.Circle_Circle_Collision(asteroid.centerpoint[0],asteroid.centerpoint[1],asteroid.size,cx,cy,cr)):
					#lose
					game_state=gs.Gamestate.GAMEOVER

			for bullet in target.bullets:
				if (Collision.AABB_Collision_rect(asteroid.getAABBShape(10),bullet.getAABBShape(10))):
					#check for colision with the asteroid and the bullets in radius
					endX,endY = bullet.getEndpoint()
					if (Collision.Circle_Line_Collision(asteroid.centerpoint[0],asteroid.centerpoint[1],asteroid.size,bullet.position[0],bullet.position[1],endX,endY)):
						print("Bullet: "+str(bullet.id)+" hitting asteroid: " +str(asteroid.id))
						bullet.die()
						score +=10
						if asteroid.hit():
							lstasteroids.remove(asteroid)
						else:
							#split asteroid into two smaller ones
							dup_asteroid = copy.deepcopy(asteroid)
							dup_asteroid.id = dup_asteroid.id+500
							asteroid.rotate(30)
							dup_asteroid.rotate(-30)
							lstasteroids.append(dup_asteroid)

	# Draw.
	if game_state==gs.Gamestate.PLAYING:
		textScore = fontScore.render("Score: "+str(score),True,(255,255,255))
		screen.blit(textScore,(20,20))
		ship.draw(screen)
		for i in lstasteroids:
			i.draw(screen)
	elif game_state==gs.Gamestate.GAMEOVER:
		screen.blit(textgameover,textgameoverRect)
		screen.blit(textreset,textresetRect)
		textScore=fontScore.render("Score: "+str(score),True,(255,255,255))
		screen.blit(textScore,(20,20))
	pygame.display.flip()
	fpsClock.tick(fps)