#!/usr/bin/env python
from time import sleep
from board import Board

def main():
	
	b = Board()
	sleepTime = 0.25
	
	while 1:
		b.startNewGame()
		pick = b.getTurn()
		if pick == 2:
			sleep(sleepTime)
			b.move()
		
		while not b.isFinished():
			pos = b.getInput()
			if pos == -1 : return
			if not b.isValid(pos): continue
			b.play(pos)
			if not b.isFinished(): 
				sleep(sleepTime)
				b.move()
	
		if b.tie(b.board):
			b.showResult(0)
		elif b.getNext(b.board) != pick:
			b.drawWinningLine()
			b.showResult(1)
		else:
			b.drawWinningLine()
			b.showResult(-1)
	
		b.end()
	
if __name__ == '__main__': main()
