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
INDIGO = 63,81,181
MBLUE = 33,150,243

MGREEN = 76,175,80
LIME =  205,220,57
AMBER = 255,193,7
ORANGE = 255,87,34
BROWN = 121,85,72
GREAY = 199,199,199
DARKLIGHTBLUE = 38,86,110
MAROON = 118,0,0


colorList = [YELLOW, MAGENTA, CYAN, RED, GREEN, PURPLE, LIME, AMBER, ORANGE, BROWN, MBLUE, MGREEN, INDIGO, GREAY, DARKLIGHTBLUE, MAROON , (36,78,56), (166,134,255)]

# could you dimanicly chang the screen size?
size = width, heights = 570, 570

pg.init()

screen = pg.display.set_mode(size)
pg.display.set_caption("Card Flip")


class Board:

	def __init__(self, amount=6,moves=40):
		self.cardNum = amount*2
		self.boardX = self.cardNum / 2
		self.boardY = self.cardNum / 3

		self.deck = []
		self.cardArrangement = []

		self.score = moves

	def setup(self):

		for x in range(self.cardNum / 2):
			self.cardArrangement.append(x)
			self.cardArrangement.append(x)

		random.shuffle(self.cardArrangement)

		# Making the cards
		for x in range(0, self.cardNum):
			self.deck.append(Card(colorList[self.cardArrangement[x]], x, self.setLocation(x)))

	def setLocation(self, x):
		y = x
		# I need to change the 60s in here to not be hard coded in later on
		if x >= 6 and x< 12:
			x = x-6
		elif x >= 12 and x<18 :
			x = x-12
		elif x >= 18 and x<24:
			x = x-18
		elif x >= 24 and x< 30:
			x = x-24
		elif x >= 30 and x<36:
			x = x-30
		return ((x + 1) * 30 + (60 * x)),(30 + 90 * (y / 6))

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


font = pg.font.SysFont('Calibri', 25, True, False)

start = True
cards = random.randint(2,18)
while start:
	welcomeScreen = font.render("Welcome to matching game.", True, BLACK)

	for event in pg.event.get():
		if event.type == pg.QUIT:
			exit()
		if event.type == pg.MOUSEBUTTONUP:
			if pg.mouse.get_pos()[0] >= 50 and pg.mouse.get_pos()[1]  >= 250 and pg.mouse.get_pos()[0] <= 500 and pg.mouse.get_pos()[1] <= 350:
				start = False
			if pg.mouse.get_pos()[0] >= 50 and pg.mouse.get_pos()[1]  >= 400 and pg.mouse.get_pos()[0] <= 140 and pg.mouse.get_pos()[1] <= 490:
				print "Easy"
				cards = 6
			if pg.mouse.get_pos()[0] >= 150 and pg.mouse.get_pos()[1]  >= 400 and pg.mouse.get_pos()[0] <= 240 and pg.mouse.get_pos()[1] <= 490:
				print "Miled"
				cards = 9
			if pg.mouse.get_pos()[0] >= 250 and pg.mouse.get_pos()[1]  >= 400 and pg.mouse.get_pos()[0] <= 340 and pg.mouse.get_pos()[1] <= 490:
				print "Spicy"
				cards = 12
			if pg.mouse.get_pos()[0] >= 350 and pg.mouse.get_pos()[1]  >= 400 and pg.mouse.get_pos()[0] <= 440 and pg.mouse.get_pos()[1] <= 490:
				print "Hot"
				cards = 18


	screen.fill(WHITE)
	screen.blit(welcomeScreen, [40, 80])
	pg.draw.rect(screen, GREEN, pg.Rect(50, 250, 450, 100))

	pg.draw.rect(screen, GREEN, pg.Rect(50, 400, 90, 90))
	pg.draw.rect(screen, YELLOW, pg.Rect(150, 400, 90, 90))
	pg.draw.rect(screen, ORANGE, pg.Rect(250, 400, 90, 90))
	pg.draw.rect(screen, RED, pg.Rect(350, 400, 90, 90))

	screen.blit(font.render("Play", True, BLACK), [250, 280])
	pg.display.flip()

game = Board(cards)

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
	if endCount == game.cardNum or game.score <= 0:
		retry = True
		while retry:

			for event in pg.event.get():
				if event.type == pg.QUIT:
					exit()
				if event.type == pg.MOUSEBUTTONUP:
					if pg.mouse.get_pos()[0] >= 50 and pg.mouse.get_pos()[1] >= 250 and pg.mouse.get_pos()[0] <= 500 and pg.mouse.get_pos()[1] <= 350:
						game = Board(cards)
						game.setup()
						retry = False
					if pg.mouse.get_pos()[0] >= 50 and pg.mouse.get_pos()[1] >= 450:
						exit()

			screen.fill(WHITE)
			if game.score <=0:
				exsitScreen= "You Lose... Would you like to play agine?"
			else:
				exsitScreen= "You got "+str(game.score) + ". Would you like to play agine?"
			screen.blit(font.render(exsitScreen, True, BLACK),[100,100])
			pg.draw.rect(screen, GREEN, pg.Rect(50, 250, 450, 100))
			pg.draw.rect(screen, RED, pg.Rect(50, 450, 450, 100))
			screen.blit(font.render("Yes", True, BLACK),[250,280])
			screen.blit(font.render("No", True, BLACK),[250,500])
			pg.display.flip()
