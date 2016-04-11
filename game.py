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

PURPLE = 156,39,176
DEEPPRUPLE = 103,58,183
INDIGO = 63,81,181
MBLUE = 33,150,243
LIGHTBLUE = 3,169,244
MCYAN = 0,188,212
TEAL = 0,150,136
MGREEN = 76,175,80
LIGHTGREEN = 139,195,74
LIME =  205,220,57
MYELLOW = 255,235,59
AMBER = 255,193,7
ORANGE = 255,87,34
BROWN = 121,85,72


colorList = [YELLOW, MAGENTA, CYAN, RED, GREEN]
mColorList = [PURPLE, DEEPPRUPLE, INDIGO, MBLUE, LIGHTBLUE , MCYAN, TEAL, MGREEN, LIGHTGREEN, LIME, MYELLOW, AMBER, ORANGE, BROWN]

# could you dimanicly chang the screen size?
size = width, heights = 570, 570

pg.init()

screen = pg.display.set_mode(size)
pg.display.set_caption("Card Flip")


class Board:

	def __init__(self):
		self.cardNum = 6
		self.boardX = self.cardNum / 2
		self.boardY = self.cardNum / 3

		self.deck = []
		self.cardArrangement = []

		self.score = 10


	def setup(self):

		for x in range(self.cardNum / 2):
			self.cardArrangement.append(x)
			self.cardArrangement.append(x)

		random.shuffle(self.cardArrangement)

		# Making the cards
		for x in range(0, self.cardNum):
			self.deck.append(Card(colorList[self.cardArrangement[x]], x, self.setLocation(x)))

	def setLocation(self, x):
		outArr = []
		y = x
		# I need to change the 60s in here to not be hard coded in later on
		if x % 6 == 0 and x != 0:
			x = 0
		outArr.append((x + 1) * 30 + (60 * x))
		outArr.append(30 + 90 * (y / 6))
		return outArr

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

font = pg.font.SysFont('Calibri', 25, True, False)

start = True
while start:
	welcomeScreen = font.render("Welcome to mathing game", True, BLACK)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()
		if event.type == pg.MOUSEBUTTONUP:
			if pg.mouse.get_pos()[0] >= 50 and pg.mouse.get_pos()[1]  >= 250 and pg.mouse.get_pos()[0] <= 500 and pg.mouse.get_pos()[1] <= 350:
				start = False

	screen.fill(WHITE)
	screen.blit(welcomeScreen, [40, 80])
	pg.draw.rect(screen, GREEN, pg.Rect(50, 250, 450, 100))
	screen.blit(font.render("Play", True, BLACK), [250, 280])
	pg.display.flip()

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


	text = font.render(str(game.score), True, BLACK)

	screen.fill(WHITE)

	screen.blit(text, [30, 0])

	for card in game.deck:
		card.drawCard()

	pg.display.flip()

	if click >= 2:
		sleep(1)
		for x in range(game.cardNum):
			game.deck[x].reset()
		click = 0
		game.score -= 1


	endCount = 0
	for card in game.deck:
		if card.found == True:
			endCount += 1
		else:
			break
	if endCount == game.cardNum:
		retry = True
		while retry:

			for event in pg.event.get():
				if event.type == pg.QUIT:
					exit()
				if event.type == pg.MOUSEBUTTONUP:
					if pg.mouse.get_pos()[0] >= 50 and pg.mouse.get_pos()[1] >= 250 and pg.mouse.get_pos()[0] <= 500 and pg.mouse.get_pos()[1] <= 350:
						game = Board()
						game.setup()
						retry = False
					if pg.mouse.get_pos()[0] >= 50 and pg.mouse.get_pos()[1] >= 450:
						exit()

			screen.fill(WHITE)
			screen.blit(font.render("you got "+str(game.score) + ". would you like to play agine?", True, BLACK),[100,100])
			pg.draw.rect(screen, GREEN, pg.Rect(50, 250, 450, 100))
			pg.draw.rect(screen, RED, pg.Rect(50, 450, 450, 100))
			screen.blit(font.render("Yes", True, BLACK),[250,280])
			screen.blit(font.render("No", True, BLACK),[250,500])
			pg.display.flip()