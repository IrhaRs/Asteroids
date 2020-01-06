import pygame
import math
from Objects import Ship

class Bullet:
	def __init__(self,x,y,direction,name,ship):
		self.position = (x,y)
		self.directionvector = direction
		self.velocity = 30
		self.color=(255,0,0)
		self.trail_length =8
		self.id = name
		self.ship = ship
		self.endvec = ((-self.directionvector[0]) *self.velocity,(-self.directionvector[1]) *self.velocity)
		self.debug = False

	def getAABBShape(self,padding):
		#get line
		beginx,beginy = self.position
		endx,endy = self.getEndpoint()
		
		ax=None 
		ay=None
		bx=None
		by=None
		#get topleft and bottom right co-ord
		if beginx<=endx:
			ax = beginx
			bx = endx
		else:
			ax = endx
			bx = beginx
		if beginy<=endy:
			ay = beginy
			by = endy
		else:
			ay = endy
			by = beginy

		return (ax - padding,ay-padding,(bx-ax)+(padding*2),(by-ay)+(padding*2))

		#return (x,y,w,h)

	def getEndpoint(self):
		x = self.position[0] + self.endvec[0]
		y = self.position[1] + self.endvec[1]
		
		#print("x: "+str(x)+" y "+ str(y))
		return(x,y)


	def draw(self,screen):
		x,y = self.getEndpoint()
		pygame.draw.line(screen,(100,100,100),self.position,(x,y),1)
				

		pygame.draw.line(screen,self.color,self.position,(self.position[0]-self.directionvector[0]*self.trail_length,self.position[1]-self.directionvector[1]*self.trail_length),3)
		
		#Collision box
		if self.debug:
			padding = 10
			x,y,w,h = self.getAABBShape(padding)
			pygame.draw.rect(screen, (0,0,255),pygame.Rect(x,y,w,h),1)


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
		self.ship.removeBullet(self.id)