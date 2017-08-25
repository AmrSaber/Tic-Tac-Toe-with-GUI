#!/usr/bin/env python
import pygame , sys
from time import sleep

#varibles 
window_width = 800
window_height = 600
box_size = 100
line_width = 10
board_width = 3
board_height = 3
margin_x = int ((window_width-(board_width*(box_size+line_width)))/2)
margin_y = int ((window_height-(board_height*(box_size+line_width)))/2)
white=(255,255,255)
black =(0,0,0)
bg_color = white
box_color = bg_color
line_color = black
Xmark = 'X'
Omark = 'O'
window = None
turn = None
sleepTime = 0.05;


#dividing board
box0 = pygame.Rect(margin_x,margin_y,box_size,box_size)
box1 = pygame.Rect(margin_x+box_size+line_width,margin_y,box_size,box_size)
box2 = pygame.Rect(margin_x+2*box_size+2*line_width,margin_y,box_size,box_size)
box3 = pygame.Rect(margin_x,margin_y+box_size,box_size,box_size)
box4 = pygame.Rect(margin_x+box_size+line_width,margin_y+box_size+line_width,box_size,box_size)
box5 = pygame.Rect(margin_x+2*box_size+2*line_width,margin_y+box_size+line_width,box_size,box_size)
box6 = pygame.Rect(margin_x,margin_y+2*box_size+2*line_width,box_size,box_size)
box7 = pygame.Rect(margin_x+box_size+line_width,margin_y+2*box_size+2*line_width,box_size,box_size)
box8 = pygame.Rect(margin_x+2*box_size+2*line_width,margin_y+2*box_size+2*line_width,box_size,box_size)

#centers determenation
centers_xy =[[margin_x+(box_size/2),margin_y+(box_size/2)],[margin_x+line_width+(3*box_size/2),margin_y+(box_size/2)],[margin_x+2*line_width+2.5*box_size,margin_y+(box_size/2)],[margin_x+(box_size/2),margin_y+3*(box_size/2)+line_width],[margin_x+line_width+3*(box_size/2),margin_y+line_width+3*(box_size/2)],[margin_x+2*line_width+2.5*box_size,margin_y+line_width+3*(box_size/2)],[margin_x+(box_size/2),margin_y+2*line_width+2.5*box_size],[margin_x+line_width+3*(box_size/2),margin_y+2*line_width+2.5*box_size],[margin_x+2.5*box_size+2*line_width,margin_y+2*line_width+5*(box_size/2)]]

#used_boxs
used_boxs = [0,0,0,0,0,0,0,0,0]

def text_objects(text,font):
	text_surface = font.render(text,True,black)
	return text_surface,text_surface.get_rect()

def init() :
	
	#initializations
	global window, turn
	pygame.init()
	window = pygame.display.set_mode((window_width,window_height))
	pygame.display.set_caption("Tic Tac Toe")
	window.fill(white)
	pygame.display.update()
	
def showLoading():
	global window
	tx = pygame.font.Font('freesansbold.ttf',30)
	txs,markR = text_objects ('Loading ...',tx)
	markR.centerx = window_width/2
	markR.centery = window_height/2
	window.blit (txs , markR)
	pygame.display.update()

def startNewGame():
	global window, turn, used_boxs
	
	#to clear all, reset the boxes and draw board
	window.fill(white)
	used_boxs = [0]*9
	turn = None
	
	#choosing
	tx = pygame.font.Font('freesansbold.ttf',30)
	txs,markR = text_objects ('Press 1 to play first or 2 to play second .',tx)
	markR.centerx = window_width/2
	markR.centery = window_height/2
	window.blit (txs , markR)
	pygame.display.update()

	while not turn :
		sleep(sleepTime)
		for event in pygame.event.get() :
			if event.type == pygame.KEYUP and (event.key==pygame.K_2 or event.key==pygame.K_KP2):
				#computer play first
				turn = 2
			elif event.type == pygame.KEYUP and (event.key==pygame.K_1 or event.key==pygame.K_KP1):
				#player play first
				turn = 1

	#to clear all and draw board
	window.fill(white)
		 
	#Horizontal lines
	left = margin_x + box_size
	top = margin_y
	width = line_width
	height = (box_size+line_width)*board_height
	rect1 = pygame.Rect(left,top,width,height)
	pygame.draw.rect(window,line_color,rect1)
	rect2 = pygame.Rect(left+box_size+line_width,top,width,height)
	pygame.draw.rect(window,line_color,rect2)

	#Vertical lines
	left = margin_x
	top = margin_y+box_size
	width = (box_size+line_width)*board_width
	height = line_width
	rect3 = pygame.Rect(left,top,width,height)
	pygame.draw.rect(window,line_color,rect3)
	rect4 = pygame.Rect(left,top+box_size+line_width,width,height)

	pygame.draw.rect(window,line_color,rect4)
	pygame.display.update()

def getTurn():
	return turn
	

def end():
	while 1 :
		sleep(sleepTime)
		for event in pygame.event.get() :
			if event.type == pygame.KEYUP:
				#pygame.quit()
				return
	
def markBox(player,box_number) :
	
	if player == 1: symbol = Xmark
	elif player == 2: symbol = Omark
	else: raise Exception('Unknonw player id')
	
	if used_boxs[box_number] == 0 :
		
		text = pygame.font.Font('freesansbold.ttf',90)
		textsurf,markRect = text_objects(symbol,text)
		markRect.centerx = centers_xy[box_number][0]
		markRect.centery = centers_xy[box_number][1]
	
		window.blit(textsurf,markRect)
		pygame.display.update()
		used_boxs[box_number] = 1
	else :
		#when a box is used and you want to mark it ... do 
		print ('used')

def result (res) :
	if res == 1 :
		txt = 'Game Over: You Win ^_^'
	elif res == -1 :
		txt = 'Game Over: You Lose :P'
	elif res == 0 :
		txt = 'Game Over: Tie'
	tx = pygame.font.Font('freesansbold.ttf',30)
	textsurf,markRect = text_objects(txt,tx)
	markRect.centerx = window_width/2
	markRect.centery = margin_y/2

	window.blit(textsurf,markRect)
	pygame.display.update()
	
def highlight (start , end) :
	pygame.draw.line(window , black , centers_xy[start], centers_xy[end],10) 
	

def takeInput():
	pygame.event.clear()
	while True :
		sleep(sleepTime)
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				pygame.quit()
				return -1
			if event.type == pygame.KEYUP and (event.key==pygame.K_7 or event.key==pygame.K_KP7):
				return 0
			elif event.type == pygame.KEYUP and (event.key==pygame.K_8 or event.key==pygame.K_KP8):
				return 1
			elif event.type == pygame.KEYUP and (event.key==pygame.K_9 or event.key==pygame.K_KP9):
				return 2
			elif event.type == pygame.KEYUP and (event.key==pygame.K_4 or event.key==pygame.K_KP4):
				return 3
			elif event.type == pygame.KEYUP and (event.key==pygame.K_5 or event.key==pygame.K_KP5):
				return 4
			elif event.type == pygame.KEYUP and (event.key==pygame.K_6 or event.key==pygame.K_KP6):
				return 5
			elif event.type == pygame.KEYUP and (event.key==pygame.K_1 or event.key==pygame.K_KP1):
				return 6
			elif event.type == pygame.KEYUP and (event.key==pygame.K_2 or event.key==pygame.K_KP2):
				return 7
			elif event.type == pygame.KEYUP and (event.key==pygame.K_3 or event.key==pygame.K_KP3):
				return 8
			#if event.type == pygame.KEYUP and event.key==pygame.K_c :
			#   clear_all()
