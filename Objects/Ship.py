import pygame
import math

class Ship:
	def __init__(self):
		self.centerpoint = (100,100) # center of the ship		
		self.rotation = -90 #rotation in degrees
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #the tip of the ship
		self.backleft=(math.cos(math.radians(self.rotation+140)),math.sin(math.radians(self.rotation+140)))
		self.backright=(math.cos(math.radians(self.rotation+220)),math.sin(math.radians(self.rotation+220)))
		self.speed = 2 #scalar velocity -> direction
		self.acceleration = 0.4
		self.velocity = 0
		self.velocitymax = 10
		self.rotationspeed = 1
		self.scale = 20
		self.color=(255,255,255)

	def shoot(self):
		#create a bullet and shoot towards self.directionvector
		pass
	def hit(self):
		#destroy ship + game over 
		pass
	def rotate(self,degrees):
		self.rotation +=degrees
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #the tip of the ship
		self.backleft=(math.cos(math.radians(self.rotation+140)),math.sin(math.radians(self.rotation+140)))
		self.backright=(math.cos(math.radians(self.rotation+220)),math.sin(math.radians(self.rotation+220)))
		print(self.rotation)

	def move(self):
		if self.velocity<self.velocitymax:
			self.velocity+=self.acceleration
		print(self.velocity)

	def loseSpeed(self):
		if self.velocity >0:
			self.velocity-= (self.acceleration*2)
		if self.velocity<0:
			self.velocity=0
		print(self.velocity)

	def update(self):
		vx = self.velocity*self.directionvector[0]
		vy = self.velocity*self.directionvector[1]

		self.centerpoint= (math.floor(self.centerpoint[0]+vx),math.floor(self.centerpoint[1]+vy))
		
	def draw(self,screen):
		#draw function manditory for objects.
		points = [(list(self.centerpoint)[0]+(list(self.directionvector)[0]*self.scale),list(self.centerpoint)[1]+(list(self.directionvector)[1]*self.scale))]
		points+= [(list(self.centerpoint)[0]+(list(self.backright)[0]*self.scale),list(self.centerpoint)[1]+(list(self.backright)[1]*self.scale))]
		points+= [(list(self.centerpoint)[0]+(list(self.backleft)[0]*self.scale),list(self.centerpoint)[1]+(list(self.backleft)[1]*self.scale))]
				
		#points = []
		#centerpointx,centerpointy = self.centerpoint
		#dvx,dvy = self.directionvector
		#blx,bly = self.backleft
		#brx,bry = self.backright
		#points.append([centerpointx+(self.scale*dvx), centerpointy+(self.scale*dvy)])
		#points.append([centerpointx+(self.scale*blx), centerpointy+(self.scale*bly)])
		#points.append([centerpointx+(self.scale*brx), centerpointy+(self.scale*bry)])


		pygame.draw.polygon(screen,self.color,points)
		pygame.draw.circle(screen, (255,0,0), self.centerpoint, 1)

