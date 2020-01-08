import pygame
import math
from Objects import Bullet
import Settings as s

class Ship:
	def __init__(self,x,y):
		self.centerpoint = (x,y) # center of the ship		
		self.rotation = -90 #rotation in degrees
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #the tip of the ship
		self.backleft=(math.cos(math.radians(self.rotation+140)),math.sin(math.radians(self.rotation+140)))
		self.backright=(math.cos(math.radians(self.rotation+220)),math.sin(math.radians(self.rotation+220)))
		self.acceleration = 0.5
		self.minvelocity=1
		self.velocity = 0
		self.velocitymax = 10
		self.rotationspeed = 1
		self.scale = 20
		self.color=(255,255,255)
		self.bullets = []
		self.bullet_count=0
		self.shootcooldown=0
		self.debug=s.DEBUG

	def shoot(self):
		if self.shootcooldown<=0:
			self.bullets.append(Bullet.Bullet(self.centerpoint[0],self.centerpoint[1],self.directionvector,self.bullet_count,self))
			self.bullet_count+=1
			self.shootcooldown=10

	def getHitbox(self):
		x,y = self.centerpoint
		return(x,y,self.scale/1.3)

	def removeBullet(self,name):
		for i in self.bullets:
			if i.id == name:
				print("delete: "+str(name))
				self.bullets.remove(i)

	def getAABBShape(self,padding):
		x =  (self.centerpoint[0]-self.scale)-padding
		y =  (self.centerpoint[1]-self.scale)-padding
		w = ((self.centerpoint[0]+self.scale)+padding) -x
		h =	((self.centerpoint[1]+self.scale)+padding) -y
		return (x,y,w,h)


	def rotate(self,degrees):
		self.rotation +=degrees
		self.directionvector = (math.cos(math.radians(self.rotation)),math.sin(math.radians(self.rotation))) #the tip of the ship
		self.backleft=(math.cos(math.radians(self.rotation+140)),math.sin(math.radians(self.rotation+140)))
		self.backright=(math.cos(math.radians(self.rotation+220)),math.sin(math.radians(self.rotation+220)))
		

	def move(self):
		if self.velocity<self.velocitymax:
			self.velocity+=self.acceleration

	def loseSpeed(self):
		if self.velocity !=0:
			if self.velocity >self.minvelocity:
				self.velocity-= (self.acceleration*(self.velocity/10))
			elif self.velocity<self.minvelocity:
				self.velocity=self.minvelocity

	def update(self):
		vx = self.velocity*self.directionvector[0]
		vy = self.velocity*self.directionvector[1]
		cx,cy=self.centerpoint
		if self.shootcooldown >0:
			self.shootcooldown-=1
		for b in self.bullets:
			b.update()
		if cx<0-10:
			cx=9+s.WIDTH
		elif cx>s.WIDTH+10:
			cx = -9
		if cy<0-10:
			cy=s.HEIGHT+9
		elif cy>s.HEIGHT+10:
			cy=-9
		self.centerpoint= (round(cx+vx),round(cy+vy))



	def draw(self,screen):
		#draw function manditory for objects.
		points = [(list(self.centerpoint)[0]+(list(self.directionvector)[0]*self.scale),list(self.centerpoint)[1]+(list(self.directionvector)[1]*self.scale))]
		points+= [(list(self.centerpoint)[0]+(list(self.backright)[0]*self.scale),list(self.centerpoint)[1]+(list(self.backright)[1]*self.scale))]
		points+= [(list(self.centerpoint)[0]+(list(self.backleft)[0]*self.scale),list(self.centerpoint)[1]+(list(self.backleft)[1]*self.scale))]

		for b in self.bullets:
			b.draw(screen)

		pygame.draw.polygon(screen,self.color,points)
		pygame.draw.circle(screen, (255,0,0), self.centerpoint, 1)


		#Collision box
		if self.debug:
			padding = 10
			x,y,w,h = self.getAABBShape(padding)
			pygame.draw.rect(screen, (0,0,255),pygame.Rect(x,y,w,h),1)
			cx,cy,cr= self.getHitbox()
			pygame.draw.circle(screen,(0,255,0),(cx,cy),math.floor(cr),1)
