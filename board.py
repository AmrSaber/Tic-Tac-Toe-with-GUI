#!/usr/bin/env python
from random import randint
from random import random as rand
import draw

class Board(object):
	def __init__(self):
		self.board = 0
		self.mem = {}
		self.sol = {}
		self.intel = 0.90
		draw.init()
		draw.showLoading()
		self.solve(0) #solves the whole board
		
	def startNewGame(self):
		self.board = 0
		draw.startNewGame()
	
	def getTurn(self):
		return draw.getTurn()
	
	def end(self):
		draw.end()
	
	def showResult(self, res):
		draw.result(res)
		
	def drawWinningLine(self):
		box1, box2 = self.getWinningBoxes()
		draw.highlight(box1,box2)
	
	def getWinningBoxes(self):
		get = self.get
		msk = self.board
		
		for i in xrange(0, 9, 3):
			if get(msk, i) == get(msk, i+1) == get(msk, i+2) != 0: return (i, i+2)
	
		for i in xrange(3):
			if get(msk, i) == get(msk, i+3) == get(msk, i+6) != 0: return (i, i+6)
	
		if get(msk, 0) == get(msk, 4) == get(msk, 8) != 0: return (0, 8)
	
		if get(msk, 2) == get(msk, 4) == get(msk, 6) != 0: return (2, 6)
		
	def getInput(self):
		while 1:
			pos = draw.takeInput()
			if pos == -1 or self.isValid(pos): return pos
		
	def move(self):
				
		solutions = self.sol[self.board]
		
		p = -1
		if rand() > self.intel:
			for i in xrange(50):	#to prevent infinite loop if all moves lead to winning state
				p = randint(0, 8)
				if self.isValid(p) and p not in solutions: break
		
		if not self.isValid(p): p = solutions[randint(0, len(solutions)-1)] 
		self.play(p)
			
		
	def play(self, pos):
		if self.get(self.board, pos) != 0: raise Exception("Can't play in a taken place")
		player = self.getNext(self.board)
		self.board = self.setMask(self.board, pos, player)
		draw.markBox(player, pos)
		draw.setAllowed() 
	
	def solve(self, msk):
		if msk in self.mem: return self.mem[msk]
		
		nxt = self.getNext(msk)
		plyr = 3 - nxt
	
		if self.tie(msk): 
			self.sol[msk] = -1
			self.mem[msk] = 0
			return 0
	
		t = self.isLosing(msk)
		if t:
			self.sol[msk] = -1
			self.mem[msk] = -1
			return -1
		
		win = []
		tie = []
		lose = []
		for i in xrange(9):
			if self.get(msk, i): continue
			s = self.solve(self.setMask(msk, i, nxt))
			if s == -1: win.append(i)
			elif s == 0: tie.append(i)
			else: lose.append(i)
	
		if len(win):
			self.sol[msk] = win
			ret = 1
		elif len(tie):
			self.sol[msk] = tie
			ret = 0
		else:
			self.sol[msk] = lose
			ret = -1
		
		self.mem[msk] = ret
		return ret
		
	#returns the number of the winner, 0 if not terminal
	def isLosing(self, msk):
		get = self.get
		ret = 3 - self.getNext(msk)
	
		for i in xrange(0, 9, 3):
			if get(msk, i) == get(msk, i+1) == get(msk, i+2) != 0: return ret
	
		for i in xrange(3):
			if get(msk, i) == get(msk, i+3) == get(msk, i+6) != 0: return ret
	
		if get(msk, 0) == get(msk, 4) == get(msk, 8) != 0: return ret
	
		if get(msk, 2) == get(msk, 4) == get(msk, 6) != 0: return ret
	
		return 0

	def tie(self, msk):
		get = self.get
		c = 0
		for i in xrange(9): c += (self.get(msk, i) > 0)
		if (c == 9) and not self.isLosing(msk): return 1
		return 0
		
	def isFinished(self):
		return self.isLosing(self.board) or self.tie(self.board)
	
	def isValid(self, pos):
		return (0 <= pos <= 8 and not self.get(self.board, pos))

	#if x is played even number next is x (1), else next is O (2)
	def getNext(self, msk):
		x = 0
		o = 0
		for i in xrange(9):
			x += (self.get(msk, i) == 1)
			o += (self.get(msk, i) == 2)
		return (x > o) + 1

	def setMask(self, msk, i, val):
		if self.get(msk, i): return msk
		return msk + val*pow(3, i)

	def get(self, msk, i):
		for j in xrange(i): msk /= 3
		return msk%3
