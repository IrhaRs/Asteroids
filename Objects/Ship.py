import pygame
import math
from Objects import Bullet

class Ship:
	def __init__(self):
		self.centerpoint = (100,100) # center of the ship		
		self.rotation = -90 #rotation in degrees
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #the tip of the ship
		self.backleft=(math.cos(math.radians(self.rotation+140)),math.sin(math.radians(self.rotation+140)))
		self.backright=(math.cos(math.radians(self.rotation+220)),math.sin(math.radians(self.rotation+220)))
		self.acceleration = 0.5
		self.velocity = 0
		self.velocitymax = 10
		self.rotationspeed = 1
		self.scale = 20
		self.color=(255,255,255)
		self.bullets = []
		self.shootcooldown=0

	def shoot(self):
		if self.shootcooldown<=0:
			self.bullets.append(Bullet.Bullet(self.centerpoint[0],self.centerpoint[1],self.directionvector))
			self.shootcooldown=10


	def hit(self):
		#destroy ship + game over 
		pass
	def rotate(self,degrees):
		self.rotation +=degrees
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #the tip of the ship
		self.backleft=(math.cos(math.radians(self.rotation+140)),math.sin(math.radians(self.rotation+140)))
		self.backright=(math.cos(math.radians(self.rotation+220)),math.sin(math.radians(self.rotation+220)))
		

	def move(self):
		if self.velocity<self.velocitymax:
			self.velocity+=self.acceleration

	def loseSpeed(self):
		if self.velocity >0:
			self.velocity-= (self.acceleration*2)
		if self.velocity<0:
			self.velocity=0

	def update(self):
		vx = self.velocity*self.directionvector[0]
		vy = self.velocity*self.directionvector[1]
		cx,cy=self.centerpoint
		if self.shootcooldown >0:
			self.shootcooldown-=1
		for b in self.bullets:
			b.update()
		if cx<0-10:
			cx=9+1000
		elif cx>1000+10:
			cx = -9
		if cy<0-10:
			cy=700+9
		elif cy>700+10:
			cy=-9
		self.centerpoint= (math.floor(cx+vx),math.floor(cy+vy))



	def draw(self,screen):
		#draw function manditory for objects.
		points = [(list(self.centerpoint)[0]+(list(self.directionvector)[0]*self.scale),list(self.centerpoint)[1]+(list(self.directionvector)[1]*self.scale))]
		points+= [(list(self.centerpoint)[0]+(list(self.backright)[0]*self.scale),list(self.centerpoint)[1]+(list(self.backright)[1]*self.scale))]
		points+= [(list(self.centerpoint)[0]+(list(self.backleft)[0]*self.scale),list(self.centerpoint)[1]+(list(self.backleft)[1]*self.scale))]

		for b in self.bullets:
			b.draw(screen)

		pygame.draw.polygon(screen,self.color,points)
		pygame.draw.circle(screen, (255,0,0), self.centerpoint, 1)

