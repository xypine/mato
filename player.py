#!/bin/python3
#written by Elias Eskelinen aka "Jonnelafin"
import mato
import time

arr = []
print("Reading file...",end="")
with open(mato.filename, "r+") as f:
	for i in f.readlines():
		arr.append(i.replace("?<", "\n"))
print("OK")
for i in arr:
	mato.nprint(i)
	time.sleep(0.01)
