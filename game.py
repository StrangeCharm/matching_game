import random
import pygame as pg

shapeList = []

# pygmae constints

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

# could you dimanicly chang the screen size?
size = width, heights = 960, 720

pg.init()

screen = pg.display.set_mode(size)
pg.display.set_caption("Card Flip")


class Board:

	def __init__(self):
		self.cardNum = 6
		self.boardX = self.cardNum / 2
		self.boardY = self.cardNum / 3
		self.deck = []
		self.board = []


	def setup(self):

		shapeList = [x for x in range(3, (self.cardNum / 2) + 3)]

		for x in range(self.cardNum / 2):
			self.board.append(x)
			self.board.append(x)

		random.shuffle(self.board)
		# Making the cards
		for x in range(0, self.cardNum):
			self.deck.append(Card(shapeList[self.board[x]], x, self.setLocation(x)))

	def setLocation(self, x):

		# I need to change the 60s in here to not be hard coded in later on
		if x < 3:
			return (x + 1) * 30 + (60 * x), 30
		elif x <= 5:
			x -= 3
			return (x + 1) * 30 + (60 * x), 120


	def printBoard(self):
		pass

	def check(self):
		# checking the first one
		for x in range(0, self.boardX):
			for y in range(0, self.boardY):
				pass

# end of Board


class Card:

	def __init__(self, shape, number, location):
		self.number = number
		self.shape = shape
		self.found = False
		self.color = BLUE
		self.x = location[0]
		self.y = location[1]
		self.xSize = 60
		self.ySize = 60

	def reset(self):
		self.color = BLUE

	def place(self, x, y):
		self.x = x
		self.y = y

	def hoverCheck(self,click):
		if pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[0] <= self.x + self.xSize and pg.mouse.get_pos()[1] <= self.y + self.ySize:
			print self.number
			self.color = WHITE
			click += 1

	def cardChek(self, nshape):
		if self.shape == nshape:
			self.found = True

	def drawCard(self):
		pg.draw.rect(screen, self.color, pg.Rect(self.x, self.y, self.xSize, self.ySize))

	def drawShape(self):
		pass

	def flip(self, flip):
		if self.found:
			# keep it flipped no matter the flip
			pass
		elif flip:
			# face up
			# Draw the card back then draw the shape
			pass
		else:
			# face down
			# Draw the card back only
			pass

# end of card


game = Board()

game.setup()

# this is the amount of clicks that the player has done
click = 0

while True:

	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()

		if event.type == pg.MOUSEBUTTONUP:
			for x in range(game.cardNum):
				game.deck[x].hoverCheck(click)

	if click > 2:
		for x in range(game.cardNum):
			game.deck[x].reset()

	screen.fill(WHITE)

	for x in range(game.cardNum):
		game.deck[x].drawCard()

	pg.display.flip()
