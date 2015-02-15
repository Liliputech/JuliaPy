# -*- coding: cp1252 -*-

from __future__ import division
from pygame import *
import colorsys
import math

black=(0,0,0)
white=(255,255,255)

w=700
z=w,w
l=[z]
d=display
s=d.set_mode(z)

#c=0.284,0.0122
#c=-0.85,0.2
c=-0.76,0.12
#c=0.35,0.05 ## forme en S
#c=-0.63,0.67 #Mettre une petite borne  #etoile de mer
#c=0.39,0.6 


borne=80

def julia(u,c):
#Indique si le complexe u appartient (True) 
#ou non (False) a J(c) 
	x,y=u
	a,b=c
	k=0
	while ((x**2+y**2) < 4):
		temp=x
		x=x**2-y**2+a
		y=2*temp*y+b
		k+=1
		if k==borne:
		    return -1
	return k

def conversion(p):
	xoffset=2
	yoffset=1.5
	xinterval=4
	yinterval=3

	i,j=p
	a=i/w * xinterval - xoffset
	b=j/w * yinterval - yoffset
	u=a,b
	return u



def hsv2rgb(h,s,v):
        return tuple(i * 255 for i in colorsys.hsv_to_rgb(h,s,v))


##def pressexit():
##        for event1 in event.get(QUIT):
##                terminate()
##        for event2 in event.get(KEYDOWN):
##                terminate()
               

def functionk(k,typ):

        if typ=='square':
                newk=k*16/borne
                newk=k**2
                return newk
        elif typ=='cube':
                newk=k*6/borne
                newk=k**3
                return newk
        elif typ=='sin':
                newk=abs(math.sin(k))
                return newk
        elif typ=='exp':
                newk=k*5/borne
                newk=math.exp(k)
                return newk
        
                
pix=range(0,w)

#if __name__=='__main__':
for i in pix:
        for j in pix:
                p=i,j
                u=conversion(p)
                k=julia(u,c)
                newk=functionk(k,'square')
                if k!=-1:
                    color=hsv2rgb(150%360,1,k/borne)
                else:
                    color=black
                s.set_at(p,color)
        d.flip()

#METTRE UNE TOUCHE EXIT

image.save(s,'fractals_julia.png')

##pressexit()
