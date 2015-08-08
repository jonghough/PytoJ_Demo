import sys
import pygame
import pytoj
from pygame.locals import *
'''
Example of using j.dll as the game logic for a simple (pointless) game.

Jon Hough
'''


screen = pygame.display.set_mode((1024, 768))
clock = pygame.time.Clock()

red = pygame.image.load('images/red.png')
blue = pygame.image.load('images/blue.png')
green = pygame.image.load('images/green.png')
yellow = pygame.image.load('images/yellow.png')
white = pygame.image.load('images/white.png')

arr = pytoj.setup_grid(5)[3]

time = 0
xindex = 0
yindex = 0

pygame.font.init()
ms = pygame.font.SysFont("monospace", 15)
title = ms.render("Rotate rows and columns to arrange the colors into the same rows.", 1, (255,255,0))


def draw(i,x,y):
        if i is 0:
                screen.blit(red,(x,y))
        elif i is 1:
                screen.blit(blue,(x,y))
        elif i is 2:
                screen.blit(green,(x,y))

        elif i is 3:
                screen.blit(yellow,(x,y))
        else:
                screen.blit(white,(x,y))

while 1:
	clock.tick(30)
	time += 30
	x=y=200
	ctr = 0
	outer = 0
	
	screen.fill((0,0,0))
	#update the blocks
	while outer < 5:
		ctr = 0
		while ctr < 5:
			draw(arr[ctr][outer],x+ctr*100,y+outer*100)
			ctr+=1
		outer+=1
	screen.blit(title,(10,10))
	
	#check if we won
	if pytoj.did_win() is 1:
		title=ms.render("You did it!", 1, (255,255,0))

	pygame.display.flip()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)			
		if not event.type == KEYDOWN: continue
		if not hasattr(event, 'key'): continue
        	if event.key == K_RIGHT:
			arr = pytoj.rotate_row(-1, yindex)[3]
			print arr
        	elif event.key == K_LEFT:
			arr = pytoj.rotate_row(1,yindex)[3]	
        		print arr
		elif event.key == K_UP: 
			arr = pytoj.rotate_column(1,xindex)[3]
        	elif event.key == K_DOWN:
			arr = pytoj.rotate_column(-1,xindex)[3]
		elif event.key == K_w:
			yindex = (yindex - 1)% 5
		elif event.key == K_s:
			yindex = (yindex + 1)% 5
		elif event.key == K_a:
			xindex = (xindex -1 )% 5
		elif event.key == K_d:
			xindex = (xindex + 1)% 5
		elif event.key == K_SPACE:
			arr = pytoj.reflect()[3]
		elif event.key == K_RETURN:
			arr = pytoj.transpose()[3]
        	elif event.key == K_ESCAPE: sys.exit(0)
 
