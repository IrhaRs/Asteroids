import pygame
import math

class Astroid:
	def __init__(self,name,rotation,x,y,size):
		self.id = name
		self.centerpoint = (x,y)
		self.rotation = rotation
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #direction of the astroid
		self.scale = 10
		self.size = size*self.scale
		self.velocity = 100/(self.size/2)
		self.color = (255,255,255)
		self.debug = True

	def hit(self):
		onDestroy=False
		if (self.size/self.scale) <=2: 
			onDestroy=True
		else:
			self.size-=self.scale
		return onDestroy

	def rotate(self,degrees):
		self.rotation +=degrees
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #the tip of the ship
		

	def getAABBShape(self,padding):
		x =  (self.centerpoint[0]-self.size)-padding
		y =  (self.centerpoint[1]-self.size)-padding
		w = ((self.centerpoint[0]+self.size)+padding) -x
		h =	((self.centerpoint[1]+self.size)+padding) -y
		return (x,y,w,h)

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


		#Collision box
		if self.debug:
			padding = 10
			x,y,w,h = self.getAABBShape(padding)
			pygame.draw.rect(screen, (0,0,255),pygame.Rect(x,y,w,h),1)
