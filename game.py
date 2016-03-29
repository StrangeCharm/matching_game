import random
import pygame as pg
from time import sleep

# pygmae constints

BLACK = 0, 0, 0
WHITE = 255, 255, 255

YELLOW = 255, 255, 0
MAGENTA = 255, 0, 255
CYAN = 0, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

BLUE = 0, 0, 255

colorList = [YELLOW, MAGENTA, CYAN, RED, GREEN]

# could you dimanicly chang the screen size?
size = width, heights = 570, 570

pg.init()

screen = pg.display.set_mode(size)
pg.display.set_caption("Card Flip")


class Board:

	def __init__(self):
		self.cardNum = 8
		self.boardX = self.cardNum / 2
		self.boardY = self.cardNum / 3

		self.deck = []
		self.cardArrangement = []

		self.score = 0


	def setup(self):

		for x in range(self.cardNum / 2):
			self.cardArrangement.append(x)
			self.cardArrangement.append(x)
		
		random.shuffle(self.cardArrangement)
		
		# Making the cards
		for x in range(0, self.cardNum):
			self.deck.append(Card(colorList[self.cardArrangement[x]], x, self.setLocation(x)))

	def setLocation(self, x):

		# I need to change the 60s in here to not be hard coded in later on
		return (x + 1) * 30 + (60 * x), 30 + 90 * (x / 6)

	def cardCheck(self):
		gameScore = 0

		for card in self.deck:
			if card.color != BLUE:
				for card2 in self.deck:

					if card.number != card2.number and card2.color != BLUE and card.cardColor == card2.cardColor and not card.found and not card2.found:
						gameScore += 1
						card.found = True
						card2.found = True

		self.score += gameScore

# end of Board


class Card:

	def __init__(self, cardColor, number, location):
		self.number = number
		self.cardColor = cardColor

		self.found = False
		# the color will indelicate of the card is flipped.
		self.color = BLUE

		self.x = location[0]
		self.y = location[1]

		self.xSize = 60
		self.ySize = 60

	def reset(self):
		if not self.found:
			self.color = BLUE

	def place(self, x, y):
		self.x = x
		self.y = y

	def hoverCheck(self):
		if pg.mouse.get_pos()[0] >= self.x and pg.mouse.get_pos()[1] >= self.y and pg.mouse.get_pos()[0] <= self.x + self.xSize and pg.mouse.get_pos()[1] <= self.y + self.ySize:
			print self.number
			self.color = self.cardColor
			return 1

	def drawCard(self):
		pg.draw.rect(screen, self.color, pg.Rect(self.x, self.y, self.xSize, self.ySize))

	def drawShape(self):
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
				try:
					click += game.deck[x].hoverCheck()
				except:
					pass

	game.cardCheck()

	font = pg.font.SysFont('Calibri', 25, True, False)
	text = font.render(str(game.score), True, BLACK)

	screen.fill(WHITE)

	screen.blit(text, [30, 30])

	for card in game.deck:
		card.drawCard()

	pg.display.flip()

	if click >= 2:
		sleep(1)
		for x in range(game.cardNum):
			game.deck[x].reset()
		click = 0
