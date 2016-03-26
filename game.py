import random ,sys
import pygame as pg


# pygmae constints

BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255

size = width,heights = 320*3, 240*3


class Board:

	def __init__(self):
		self.cardNum = 6
		self.boardX = self.cardNum / 2
		self.boardY = self.cardNum / 3
		self.deck = []
		self.board = []

		self.shapeList = [x for x  in range(3,(self.cardNum/2)+3)  ]



	def setup(self):

		random.shuffle(self.board)

		for x in range(self.cardNum/2):
			self.board.append(x)
			self.board.append(x)

		# Making the cards
		for x in range(self.cardNum):
			self.deck.append(self.shapeList[],x)


	def printBoard(self):
		pass

	def check(self):
		# checking the first one
		for x in range(0,self.boardX):
			for y in range(0,self.boardY):
				pass

	for x in (0,3,6,9):
		board.append([randBoard[x],randBoard[x+1],randBoard[x+2]])
	#board.append([randBoard[0],randBoard[1],randBoard[2]])
	#board.append([randBoard[3],randBoard[4],randBoard[5]])
	#board.append([randBoard[6],randBoard[7],randBoard[8]])
	#board.append([randBoard[9],randBoard[10],randBoard[11]])

#end of Board

class card:

	def __init__(self, shape, number):
		self.number = number
		self.shape = shape[0]
		self.points = shape[1]
		self.found = False
		self.color = BLUE
		self.x = 0
		self.y = 0

	def reset(self):
		self.color = BLUE

	def place(self,x,y):
		self.x = x
		self.y = y

	def hoverCheck(self):
		if pg.mouse.get_pos()[0] >= 30 and pg.mouse.get_pos()[1] >= 30 and  pg.mouse.get_pos()[0] <= 90 and pg.mouse.get_pos()[1] <= 90 :
			print "1"
			self.color=WHITE
			click+=1

	def cardChek(self,nShape):
		if self.shape == nShape:
			self.found = True

	def draw(self):
		pg.draw.rect(screen, c1, pg.Rect(self.x, self.y, 60, 60))


	def flip(self,bool):
		if self.found == True:
			#keep it fliped nomatter the bool
			pass
		elif bool == True:
			# face up
			pass
		elif bool == False:
			# face down
			pass
		else:
			#Just incase

			raise Exception("No card input")

#end of card

pg.init()

screen = pg.display.set_mode(size)
pg.display.set_caption("Card Bard")
game = Board()

game.shuffle()
#pygame

#this is the amount of clicks that the playr has done
click = 0

while False:

	font = pg.font.SysFont('Calibri', 25, True, False)

	title = font.render("SplashScreen.png", True, BLACK)

	playerName = raw_input("what is your name\n>")
	name = font.render(playerName, True, BLACK)


	screen.fill(WHITE)
	screen.blit(title, [200, 200])
	screen.blit(name, [200, 500])
	pg.display.flip()
	break


while True:

	for event in pg.event.get():
		if event.type == pg.QUIT:
			sys.exit()

		if event.type == pg.MOUSEBUTTONUP:
			pass
			#for loop over the card spots
			#card.check

	if clik > 2:
		pass

#PG display
	#font = pg.font.SysFont('Calibri', 25, True, False)
	#text = font.render("SplashScreen.png", True, BLACK)

	screen.fill(WHITE)
	#screen.blit(text, [200, 200])


	pg.display.flip()
