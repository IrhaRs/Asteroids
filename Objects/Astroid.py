import pygame
import math

class Astroid:
	def __init__(self,rotation,x,y,size):
		self.centerpoint = (x,y)
		self.rotation = rotation
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #direction of the astroid
		self.size = size
		self.velocity = 100/(size/2)
		self.color = (255,255,255)


	def hit(self):
		#get hit
		pass
	def split(self):
		#split the astroid into two smaller ones.
		pass

	def update(self):
		vx = self.velocity*self.directionvector[0]
		vy = self.velocity*self.directionvector[1]
		cx,cy=self.centerpoint

		if cx<0-self.size:
			cx = 1000+self.size-1
		elif cx>1000+self.size:
			cx=0-self.size+1
		if cy<0-self.size:
			cy=self.size+700-1
		elif cy>700+self.size:
			cy = 0-self.size+1

		self.centerpoint= (math.floor(cx+vx),math.floor(cy+vy))


	def draw(self,screen):

		pygame.draw.circle(screen, self.color, self.centerpoint, self.size,2)

