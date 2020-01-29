#!/bin/python3
#written by Elias Eskelinen aka "Jonnelafin"
import os, copy, sys
import random
def rnd(f, t):
	return random.randint(f, t)
from curtsies import Input
print("Initializing mato...")
x = 1
y = 1
arr = []
locs = []
t = 0


#P
p_treat = "*"
p_snake = "."
p_empty = " "


filename = "best.replay"

arr_show = arr
rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows) - 5
columns = int(columns) - 4

rows = int(rows)
columns = int(columns)
tail = 3
m = 1
score = 0
hscore = 0
dead = False

record = []
best = []

treat = (rnd(3, rows), rnd(3, columns))

limitBounds = True

def zero():
	global x, y, tail, m, score, vx, vy, delay, delta, columns, rows, record, best
	if hscore == score:
		#best = copy.deepcopy(record)
		save(record)
	record = []
	x = 3
	y = 3
	x = int(rows / 2)
	y = int(columns / 2)
	tail = 3
	m = 1
	score = 0
	vx = 0
	vy = 0
	clear()
	#delay = 0.05
	#delta = 0
#delay = 0.5 - int(0.01 * m)
delay = 0.05
delta = 0
vx = 0
vy = 0
def clear():
	global arr, rows, columns, p_empty
	arr = []
	for i in range(int(rows)):
		row = []
		for i in range(int(columns)):
			row.append(p_empty)
		arr.append(row)
for i in range(int(rows)):
	row = []
	for i in range(int(columns)):
		row.append(p_empty)
	arr.append(row)

arr[int(rows/2)-3][int(columns/2)] = "w"
arr[int(rows/2)][int(columns/2)-3] = "a"
arr[int(rows/2)+3][int(columns/2)] = "s"
arr[int(rows/2)][int(columns/2)+3] = "d"
print("Init complete.")

def cls():
	print("\033[H\033[J")
def nprint(ar):
	out = ""
	#out = "-"*columns + "\n"
	for i in ar:
		out = out + "|"
		for x in i:
			out = out + x
		out = out + "|\n"
	#out = out + "-"*columns + "\n"
	#print("\033[H\033[J")
	cls()
	print(" " + "-"*(columns) + " ")
	print(out, end="")
	print(" " + "-"*(columns) + " ")
	return out
#	for i in ar:
#		for x in i:
#			print(x,end="")
#		print()


def safeM():
	global x, y, vx, vy, columns, rows
	global p_treat, p_snake, p_empty
	rev = False
	if x > 0 and x < rows - 1:
		x = x + vx
	else:
		vx = vx * -1
		x = x + vx
		rev = True
	if y > 0 and y < columns-1:
		y = y + vy
	else:
		rev = True
		vy = vy * -1
		y = y + vy
	return rev
def block():
	global x, y, columns, rows, arr, vx, vy
	global p_treat, p_snake, p_empty
	die = False
	
	if x < 0:
		x = 0
		die = True
	if y < 0:
		y = 0
		die = True
	if y > columns - 1:
		y = columns - 1
		die = True
	if x > rows - 1:
		x = rows - 1
		die = True
	if die:
		return die
	try:
		if arr[x+vx][y+vy] == p_snake and vx+vy != 0:
			die = True
	except Exception as e:
		e = ""
	try:
		if arr[x][y] == p_treat:
			doScore()
	except Exception as e:
		e = ""
	return die
def doScore():
	global m, treat, rows, columns, arr, tail, delay, score, hscore
	global p_treat, p_snake, p_empty
	m = m * 2
	tail = tail + 1
	arr[treat[0]][treat[1]] = p_empty
	treat = (rnd(1, rows-2), rnd(1, columns-2))
	delay = delay * 0.9
	mx = (2000000 - delta)
	if(mx < 0):
		mx = 0
	score = score + int(int(m*mx)/100000)
	if score > hscore:
		hscore = score
	#delta
def end(msg, askRetry = False):
	global x, y
	print(msg + "(" +str(x) + "," + str(y) + ")")
	print("Have a good day!")
	if not askRetry:
		sys.exit()
	title(msg)
def save(arr):
	cls()
	an = ["|", "/", "-", "\\"]
	out = ""
	with open(filename, "w+") as f:
		for i in arr:
			cls()
			an.append(an.pop(0))
			print("please wait, saving your run..." + an[0])
			z = ""
			for x in i:
				z = z + str(x)
			out = out + z.replace("\n", "?<") + "\n"
			#f.write(str(i))
		f.write(out)
		f.close()
	cls()
	print("please wait, saving your run..." + "DONE")
def step(c, autoR = False, render = True, printC = False, printXY = False, printS = True):
	global m, treat, rows, columns, arr, tail, delay, score, t, delta, vx, vy, m, dead, x, y
	global p_treat, p_snake, p_empty
	global record
	#print("Not implemented yet!")
	try:
		arr[locs[t-tail][0]][locs[t-tail][1]] = p_empty
	except Exception as e:
		print(e)
	#c = input.send(delay)
	if c == "w" and vx != 1:
		vy = 0
		vx = -1
	elif c == "s" and vx != -1:
		vy = 0
		vx = 1
	elif c == "a" and vy != 1:
		vy = -1
		vx = 0
	elif c == "d" and vy != -1:
		vy = 1
		vx = 0
	elif c == "e":
		for i in range(5):
			#t = t + 1
			#tail = tail - 1
			x = x + vx
			y = y + vy
			#locs.append([x, y])
	elif c == "q":
		#break
		end("User exit")
	elif c == "r":
		arr[treat[0]][treat[1]] = p_empty
		treat = (rnd(1, rows-2), rnd(1, columns-2))
	#with Input(keynames='curses') as input_generator:
	#	for e in input_generator:
	#		print(repr(e))
	arr_show = arr.copy()[:]
	#arr_show = copy.deepcopy(arr)
	rev = False
	rev = safeM();
	if rev and not autoR:
		end("You died.", True)
	if rev and autoR:
		#zero()
		dead = True
		#end("You died.", False)
	#if rev:
		#vy = vy * -1
		#vx = vx * -1
		#safeM();
	rev = block()
	try:
		arr[treat[0]][treat[1]] = p_treat
	except Exception as e:
		e = ""
		treat = (rnd(1, rows-2), rnd(1, columns-2))
	if rev and not autoR:
		end("You died.", True)
	if rev and autoR:
		#zero()
		dead = True
		#end("You died.", False)
	
	arr_show[x][y] = p_snake
	#os.system("clear")
	arr_show = copy.deepcopy(arr)
	
	if render:
		nprint(arr_show)
		if printS:
			print("score: " + str(int(score)) + ", " + str(m) + p_snake)
		if printC:
			print("Char: " + c)
		if printXY:
			print("XY: " + str(x) + "," + str(y))
	t = t + 1
	delta = delta + 1
	#score = score + int(t*m)
	locs.append([x, y])
	record.append(arr_show)
def main():
	global m, treat, rows, columns, arr, tail, delay, score, t, delta, vx, vy, m
	global p_treat, p_snake, p_empty
	with Input(sys.stdin) as input:
		while True:
			c = input.send(delay)
			step(c)
def title(title = "MATO"):
	global score, hscore
	cls()
	msg1 = "PRESS ENTER TO START"
	fill = " " * int(columns / 2 - len(msg1)/2)
	msg = "MATO by Jonnelafin" + "\n" * int(rows/2) + fill + title + "\n" + fill + msg1 + "\n" + fill + "SCORE: " + str(score) + "\n" + fill + "HISCORE: " + str(hscore) + "\n" * int(rows/2 - 4)
	zero()
	print(msg)
	print("enter + q to quit")
	inp = input()
	if inp == "q":
		end("User exit")
	main()
if __name__ == '__main__':
	title()
	#main()
