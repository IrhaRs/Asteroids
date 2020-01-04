import pygame
import math

class Bullet:
	def __init__(self,x,y,direction):
		self.position = (x,y)
		self.directionvector = direction
		self.velocity = 30
		self.color=(255,0,0)
		self.trail_length =5

	def draw(self,screen):
		pygame.draw.line(screen,self.color,self.position,(self.position[0]-self.directionvector[0]*self.trail_length,self.position[1]-self.directionvector[1]*self.trail_length),2)

	def update(self):
		vx = self.velocity*self.directionvector[0]
		vy = self.velocity*self.directionvector[1]
		cx,cy=self.position

		if cx<0-10:
			self.die()
		elif cx>1000+10:
			self.die()
		if cy<0-10:
			self.die()
		elif cy>700+10:
			self.die()
		self.position= (math.floor(cx+vx),math.floor(cy+vy))


	def die(self):
		del self