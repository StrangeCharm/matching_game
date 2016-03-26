import random ,sys
import pygame as pg

# game vars

board = []
randBoard = [1,1,2,2,3,3,4,4,5,5,6,6]

finishedBoard = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
# pygmae constints

BLACK = 0,0,0
WHITE = 255,255,255
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255

# this is where the amount of vertisies that each shape will have will be pulled from
polyPoints = (3,4,5,6,7,8)

size = width,heights = 320*3, 240*3

cardNum = 6

class Board:

    def __init__(self):
        self.boardX = 4
        self.boardY = 3

    def printBoard(self):
        pass

    def silect(self, x, y):
        if finishedBoard[x][y] == 0:
            finishedBoard[x][y] += board[x][y]

    def check(self):
        matches=0
        # checking the first one
        for x in range(0,self.boardX):
            for y in range(0,self.boardY):
                # checkig the secund one
                for a in range(0,self.boardX):
                    for b in range(0,self.boardY):

                        if finishedBoard[x][y] == finishedBoard[a][b]:
                            if finishedBoard[x][y] != 0:
                                if x != a or y!=b:
                                    print "Match Found"
                                    matches+=1
            return matches
    def shuffle(self):
        random.shuffle(randBoard)
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

deck = []
for x in range(cardNum):
    deck.append(,x)


while True:

	for event in pg.event.get():
		if event.type == pg.QUIT: sys.exit()

		if event.type == pg.MOUSEBUTTONUP:

			#for loop over the card spots
            #card.check


	#game eliments
	#game.printBoard()
		#for testing only
	#game.silect(int(raw_input("x>"))-1,int(raw_input("y>"))-1)
	#print game.check()


	if board == finishedBoard:
		break

    if clik > 2:
        pass

#PG display
	#font = pg.font.SysFont('Calibri', 25, True, False)
	#text = font.render("SplashScreen.png", True, BLACK)

	screen.fill(WHITE)
	#screen.blit(text, [200, 200])


	pg.display.flip()
