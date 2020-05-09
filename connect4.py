import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

ROW_C = 6
COLUMN_C = 7

myfont = pygame.font.SysFont("lato", 55)

BOXSIZE = 100
game_over = False
turn = 0
count=0
width = COLUMN_C * BOXSIZE +300#COLUM=7
height = (ROW_C) * BOXSIZE #ROW=6

message_width = COLUMN_C * BOXSIZE
message_height = 250

size = (width, height)
RADIUS = int(BOXSIZE/2 - 15)
screen = pygame.display.set_mode(size)
def create_canvas():
	canvas = np.zeros((ROW_C+1,COLUMN_C))
	return canvas

def drawCircle(canvas, row, col, element):
	canvas[row][col] = element

def isNotEmpty(canvas, col):
    return canvas[ROW_C-1][col] == 0

def get_next_open_row(canvas, col):
	for r in range(ROW_C):
		if canvas[r][col] == 0:
			return r

def print_canvas(canvas):
	print(np.flip(canvas, 0))





def checkWinner(canvas, element): 
    # case NS-WE

	for c in range(COLUMN_C-3):
		for r in range(3, ROW_C):
			if canvas[r][c] == element and canvas[r-1][c+1] == element and canvas[r-2][c+2] == element and canvas[r-3][c+3] == element:
				label=myfont.render("Game over!",1,WHITE)
				screen.blit(label,(int(message_width+50),int(message_height-100)))

				label=myfont.render("case NS-WE",1,WHITE)
				screen.blit(label,(int(message_width+30),message_height))

				return True
	# case W-E
	for c in range(COLUMN_C-3): #
		for r in range(ROW_C):
			if canvas[r][c+3] == element and canvas[r][c+2] == element and canvas[r][c+1] == element and canvas[r][c] == element:
				label=myfont.render("Game over!",1,WHITE)
				screen.blit(label,(int(message_width+50),int(message_height-100)))
				label=myfont.render("case W-E",1,WHITE)
				screen.blit(label,(int(message_width+70),message_height))
				return True

	

	# case SW-NE

	for c in range(COLUMN_C-3):
		for r in range(ROW_C-3):
			if canvas[r][c] == element and canvas[r+1][c+1] == element and canvas[r+2][c+2] == element and canvas[r+3][c+3] == element:
				label=myfont.render("Game over!",1,WHITE)
				screen.blit(label,(int(message_width+50),int(message_height-100)))

				label=myfont.render("case SW-NE",1,WHITE)
				screen.blit(label,(int(message_width+30),message_height))

				return True
    # case N-S
	for c in range(COLUMN_C):
		for r in range(ROW_C-3):
			if canvas[r][c] == element and canvas[r+1][c] == element and canvas[r+2][c] == element and canvas[r+3][c] == element:
				label=myfont.render("Game over!",1,WHITE)
				screen.blit(label,(int(message_width+50),int(message_height-100)))
				label=myfont.render("case N-S",1,WHITE)
				screen.blit(label,(int(message_width+70),message_height))
				return True


def draw_canvas(canvas):
	for c in range(COLUMN_C):
		for r in range(ROW_C):
			pygame.draw.rect(screen, BLUE, (c*BOXSIZE, r*BOXSIZE, BOXSIZE, BOXSIZE))
			pygame.draw.circle(screen, WHITE, (int(c*BOXSIZE+BOXSIZE/2), int(r*BOXSIZE+BOXSIZE/2)), RADIUS)
			
			
	for c in range(COLUMN_C):

		for r in range(ROW_C):		

			if canvas[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*BOXSIZE+BOXSIZE/2), height-int(r*BOXSIZE+BOXSIZE/2)), RADIUS)

			elif canvas[r][c] == 2:
				pygame.draw.circle(screen, YELLOW, (int(c*BOXSIZE+BOXSIZE/2), height-int(r*BOXSIZE+BOXSIZE/2)), RADIUS)

	pygame.display.update()

canvas = create_canvas()
print_canvas(canvas)
pygame.init()



draw_canvas(canvas)
pygame.display.update()

while not game_over:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.QUIT
		

		pygame.display.update()


		if event.type == pygame.MOUSEBUTTONDOWN:

			if turn == 0:
				label=myfont.render("RED turn",1,BLACK)
				screen.blit(label, (770,50))
				label=myfont.render("YELLOW turn",1,YELLOW)
				screen.blit(label, (730,50))
				posx = event.pos[0]
				col = int(math.floor(posx/BOXSIZE))

				if isNotEmpty(canvas, col):
					row = get_next_open_row(canvas, col)
					drawCircle(canvas, row, col, 1)

					if checkWinner(canvas, 1):
						label = myfont.render("Red  win !!!", 1, RED)
						screen.blit(label, (750,350))

						label = myfont.render("Congratulation!", 1, RED)
						screen.blit(label, (700,450))

						game_over = True

			else:				
				label=myfont.render("YELLOW turn",1,BLACK)				
				screen.blit(label, (730,50))			
				label=myfont.render("RED turn",1,RED)				
				screen.blit(label, (770,50))				
				posx = event.pos[0]
				col = int(math.floor(posx/BOXSIZE))



				if isNotEmpty(canvas, col):

					row = get_next_open_row(canvas, col)
					drawCircle(canvas, row, col, 2)

					if checkWinner(canvas, 2):
						label = myfont.render("Yellow win !!!", 1, YELLOW)
						screen.blit(label, (730,350))

						label = myfont.render("Congratulation!", 1, YELLOW)
						screen.blit(label, (700,450))

						game_over = True
			print_canvas(canvas)
			draw_canvas(canvas)
			turn += 1
			turn = turn % 2



			if game_over:
				pygame.time.wait(6000)
