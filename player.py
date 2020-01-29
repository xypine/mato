#!/bin/python3
#written by Elias Eskelinen aka "Jonnelafin"
import mato
import time, sys

t = 0
arrt = []
treats = []

#sys.exit()

print("Reading file...",end="")
with open(mato.filename, "r+") as f:
	x = 0
	y = 0
	for i in f.readlines():
		i = i.replace("\n", "")
		if i[0] == "#":
			mato.hiscore = int(i.split("#")[1])
		elif i[0] == "(":
			line = i.replace("(", "").replace(")","")
			x = int(line.split(",")[0])
			y = int(line.split(",")[1])
			treats.append( [x, y] )
		elif i == "None":
			arrt.append("")		
			t = t + 1
			treats.append( [x, y] )
		else:
			#print("key record " + str(t) + " found")
			arrt.append(i)		
			t = t + 1
			treats.append( [x, y] )
		


print("OK")
print(str(t) + " lines in total.")
mato.zero(False)
for i in range(t):
	
	
	mato.treat = treats[i]
#	mato.treat = treats[t][1]	
	mato.step(str(arrt[i]), True, True, True, False, False)
	print("frame " + str(i))
	mato.arr[treats[i][0]][treats[i][1]] = mato.p_empty
	#print("Key: " + str(arrt[i]))
	#time.sleep(1)
	#t = t + 1

