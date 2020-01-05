import math


def Circle_Circle_Collision(c1x,c1y,c1r,c2x,c2y,c2r):
	#circle to circle Collision 
	pass

def Circle_Line_Collision(cx,cy,cr,lsx,lsy,lex,ley):
	#circle to line/vector segment Collision 
	pass

def AABB_Collision(x1,y1,w1,h1,x2,y2,w2,h2):
	if (x1<x2 + w2 and x1 + w1 > x2 and y1<y2+h2 and y1+h1 > y2):
		print("Collision Detected!")
		return true



