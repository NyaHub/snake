import sys
import pygame
import random as r
from pygame.constants import *


snake = [[10,7],[10,8]]
snakeV = [1,0]
apple = [0,0]

def revsort(list):
	list2 = [0 for i in range(len(list))]
	for i in range(len(list)):
		list2[-i-1] = list[i]
	return list2

pygame.init()
pygame.font.init()

win = pygame.display.set_mode((300,300))
font = pygame.font.SysFont("sans", 12)
clock = pygame.time.Clock()

def mapload(path):
	maps = pygame.Surface((300,300),pygame.SRCALPHA)
	mapsv = []
	maps.fill((0,0,0,0))
	cell = pygame.Surface((10,10))
	cell.fill((200,200,10))
	file = open(path,"r")
	for i in range(30):
		f = file.readline()
		for j in range(len(f)):
			if(f[j]=="*"):
				maps.blit(cell,(i*10,j*10))
				mapsv.append([i,j])
	file.close()
	return maps,mapsv

maps,mapsv = mapload("map.txt")
win.blit(maps,(0,0))

def loop():
	global apple
	oldsnake = snake[0]

	newS = [snake[-1][0]+snakeV[0],snake[-1][1]+snakeV[1]]
	if (newS in snake) or (newS in mapsv):
		print("gameOver")
		return True
	if newS[0]>30:
		newS[0] = 0
	if newS[0]<0:
		newS[0] = 30
	if newS[1]>30:
		newS[1] = 0
	if newS[1]<0:
		newS[1] = 30
	snake.append(newS)
	snakeSurf = pygame.Surface((10,10))
	snakeSurf.fill((255,255,255))
	win.blit(snakeSurf, (snake[-1][0]*10,snake[-1][1]*10))
	snakeSurf.fill((200,0,0))
	win.blit(snakeSurf, (apple[0]*10,apple[1]*10))
	if apple in snake:
		while True:
			apple = [r.randint(0,30),r.randint(0,30)]
			if not ((apple in snake) or (apple in mapsv)):
				break
		return
	snake.remove(snake[0])
	snakeSurf.fill((0,0,0))
	win.blit(snakeSurf,(oldsnake[0]*10,oldsnake[1]*10))



loose = False
while True:

	e = pygame.event.get()
	for i in e:
		if i.type==QUIT or (i.type==KEYDOWN and i.key==K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif i.type==KEYDOWN:
			if i.key==K_UP:
				if(snakeV[1]==1):
					snake = revsort(snake)
				snakeV[1] = -1
				snakeV[0] = 0
			elif i.key==K_DOWN:
				if(snakeV[1]==-1):
					snake = revsort(snake)
				snakeV[1] = 1
				snakeV[0] = 0
			if i.key==K_RIGHT:
				if(snakeV[0]==-1):
					snake = revsort(snake)
				snakeV[0] = 1
				snakeV[1] = 0
			elif i.key==K_LEFT:
				if(snakeV[0]==1):
					snake = revsort(snake)
				snakeV[0] = -1
				snakeV[1] = 0
	
	if not loose:
		win.blit(maps,(0,0))
		loose = loop()

	pygame.display.update()
	clock.tick(10)