#!/bin/python3
#written by Elias Eskelinen aka "Jonnelafin"
import mato
import time, sys

t = 0
arrt = []
treats = []
le = []

#sys.exit()
l = "2"
print("Reading file...",end="")
lc = 0
with open(mato.filename, "r+") as f:
	x = 0
	y = 0
	for i in f.readlines():
		i = i.replace("\n", "")
		if len(i) == 0:
			arrt.append("")
			treats.append( [x, y] )
			le.append(l)
		elif i[0] == "#":
			mato.hiscore = int(i.split("#")[1])
		elif i[0] == "(":
			line = i.replace("(", "").replace(")","")
			x = int(line.split(",")[0])
			y = int(line.split(",")[1])
#			treats.append( [x, y] )
#			le.append(l)
		elif i[0] == "!":
			lc = lc + 1
#			le.append(i.replace("!", ""))
			l = i.replace("!","")
#			treats.append( [x, y] )
		elif i == "None":
			arrt.append("")
			t = t + 1
			le.append(l)
			treats.append( [x, y] )
		else:
			#print("key record " + str(t) + " found")
			arrt.append(i)
			t = t + 1
			treats.append( [x, y] )
			le.append(l)
print("OK")
print(str(t) + " frames in total.")
print(str(len(le)) + " tail records in total, which of " + str(lc) + " are real.")
print(str(len(treats)) + " treat records in total")
mato.zero(False)
input("press enter to continue\n>")
import time
for i in range(t):
	mato.treat = treats[i]
#	mato.treat = treats[t][1]	
	mato.tail = int(le[i])
	mato.step(str(arrt[i]), True, True, True, False, False)
	print("frame " + str(i))
	try:
		mato.arr[treats[i][0]][treats[i][1]] = mato.p_empty
	except Exception as e:
		e = ""
	#print("Key: " + str(arrt[i]))
	#time.sleep(1)
	#t = t + 1
	time.sleep(0.01)
