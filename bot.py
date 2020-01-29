#!/bin/python3
#written by Elias Eskelinen aka "Jonnelafin"
import mato, time
import math

k = ["a", "w", "s", "d", ""]


def dist(x1,y1,x2,y2):  
     distt = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return distt
def cToXY(c):
	global mato
	x = mato.vy
	y = mato.vx
	if c == "":
		x = mato.vx
		y = mato.vy
	if c == "w":
		x = -1
		y = 0
	if c == "s":
		x = 1
		y = 0
	if c == "a":
		y = -1
		x = 0
	if c == "d":
		y = 1
		x = 0
	return x, y
it = 1
iterations = 200
mato.zero()
slee = 0
ls = 20000000
for t in range(iterations):
	for i in range(it):
		#r = mato.rnd(0, len(rules)-1)
		mato.dead = False
		while True:
			c = k[mato.rnd(0, len(k)-1)]
			s = 20000
			for d in k:
				x, y = cToXY(d)
				ds = dist(x + mato.x, y + mato.y, mato.treat[0], mato.treat[1])
				#ds = (mato.treat[0] - (mato.vx + x)) + (mato.treat[1] - (mato.vy + y))
				if ds <= s:
					c = d
					s = ds
			if s > ls:
				c = "r"
				#c2 = ""
#				if c == "a":
#					c2 = "w"
#				elif c == "d":
#					c2 = "s"
#				elif c == "s":
#					c2 = "a"
#				elif c == "w":
#					c2 = "d"
				#if c == "" and mato.vx == 1:
				#	c2 = "w"
				#elif c == "" and mato.vx == -1:
				#	c2 = "s"
				#elif c == "" and mato.vy == 1:
				#	c2 = "a"
				#elif c == "" and mato.vx == -1:
				#	c2 = "d"
				#step(c2, True, False)
			#if (mato.treat[0] - (mato.x + 1)) < (mato.treat[0] - mato.x):
			#	c = "d"
			#if (mato.treat[0] - (mato.x - 1)) < (mato.treat[0] - mato.x):
			#	c = "a"
			#if (mato.treat[1] - (mato.y + 1)) < (mato.treat[1] - mato.y):
			#	c = "w"
			#if (mato.treat[1] - (mato.y - 1)) < (mato.treat[1] - mato.y):
			#	c = "s"
			#while (mato.x + mato.vx <= 1 and not (c==" " or c=="w")) or (mato.x + mato.vx > mato.rows - 3 and not (c==" " or c=="s")):
				#c = "d"
			#	c = k[mato.rnd(0, len(k)-1)]
			while ((c == "w" or c== "") and (mato.x + -1 <= 2)) or ((c == "s" or c== "") and (mato.x + 1 >= mato.rows -2)):
				c = k[mato.rnd(0, len(k)-1)]
			#while (c == "s" or c== "") and (mato.x + 2 >= mato.rows -4):
			#	c = k[mato.rnd(0, len(k)-1)]
			while ((c == "a" or c== "") and (mato.y + -1 <= 2)) or ((c == "d" or c== "") and (mato.y + 1 >= mato.columns -2)):
				c = k[mato.rnd(0, len(k)-1)]
			#while (c == "d" or c== "") and (mato.y + 2 >= mato.columns -4):
			#	c = k[mato.rnd(0, len(k)-1)]
			#print("VX: " + str(mato.vx) + ", X: " + str(mato.x) + ", add: " + str(mato.x + mato.vx))
			if s >= ls:
				#mato.zero()
				c = "r"
			mato.step(c, True, False, True, True, False)
			#print(s)
			if mato.dead:
				#mato.end("f")
				#mato.zero()
				break
			ls = s
			if(slee > 0):
				time.sleep(slee)
	print("Iteration " + str(t) + " done, score: " + str(mato.score))
	mato.zero()
print(str(iterations) + " iterations done, best score: " + str(mato.hscore))
conf = input("Play the best iteration? (y/*)\n>")
if conf == "y":
	for i in mato.best:
		mato.nprint(i)
		#time.sleep(0.01)
