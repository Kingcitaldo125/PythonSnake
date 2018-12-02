import random
import time
import pygame


retroMode = int(raw_input("Retro Mode? 1 for yes 0 for no\n"))


def main():
	global retroMode
	
	pygame.display.init()

	winx = 800
	winy = 600

	screen = pygame.display.set_mode((winx,winy))

	clock = pygame.time.Clock()
	
	# Snake Color
	snake_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
	
	# Food Color
	food_color = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))

	# Defaults
	defaultLength = 4
	defaultDirection = 2

	squareSize = 15
	squareList = []

	startX = 400
	startY = 300

	for i in range(defaultLength):
		squareList.append([startX,startY])
		startY += squareSize+1

	foodX = random.randint(1, winx-(squareSize-1))
	foodY = random.randint(1, winy-(squareSize-1))

	previousX = squareList[0][0]
	previousY = squareList[0][1]

	sleepTime = 0.15

	direction = defaultDirection
	squareIndex = 1
	done = False

	while not done:
		# Update
		
		leadX = squareList[0][0]
		leadY = squareList[0][1]
		
		previousX = squareList[0][0]
		previousY = squareList[0][1]
		
		if direction == 0: # up
			squareList[0][1] -= (squareSize+1)
		elif direction == 1: # down
			squareList[0][1] += (squareSize+1)
		elif direction == 2: # left
			squareList[0][0] -= (squareSize+1)
		else: #right
			squareList[0][0] += (squareSize+1)
			
		# Display Loose Animation Sequence
		if leadX+squareSize+1 > winx or leadX <= 0 or leadY+squareSize+1 > winy or leadY <= 0:
			time.sleep(0.5)
			screen.fill((0,0,0))
			pygame.display.flip()
			time.sleep(0.5)
			screen.fill((255,0,0))
			pygame.display.flip()
			time.sleep(0.5)
			screen.fill((0,0,0))
			pygame.display.flip()
			time.sleep(0.5)
			screen.fill((255,0,0))
			pygame.display.flip()
			time.sleep(0.5)
			screen.fill((0,0,0))
			pygame.display.flip()
			time.sleep(1)
			print("You Loose..")
			done = True
			
		if len(squareList) > 4:
			for sqq in range(1,len(squareList)):
				if leadX+squareSize >= squareList[sqq][0] and leadX <= squareList[sqq][0]+squareSize and leadY+squareSize > squareList[sqq][1] and leadY <= squareList[sqq][1]+squareSize:
					time.sleep(0.5)
					screen.fill((0,0,0))
					pygame.display.flip()
					time.sleep(0.5)
					screen.fill((255,0,0))
					pygame.display.flip()
					time.sleep(0.5)
					screen.fill((0,0,0))
					pygame.display.flip()
					time.sleep(0.5)
					screen.fill((255,0,0))
					pygame.display.flip()
					time.sleep(0.5)
					screen.fill((0,0,0))
					pygame.display.flip()
					time.sleep(1)
					print("You Loose..")
					done = True
		if done:
			break
			
		if leadX+squareSize >= foodX and leadX <= (foodX+squareSize):
			if leadY+squareSize >= foodY and leadY <= (foodY+squareSize):
				foodX = random.randint(1, winx-(squareSize-1))
				foodY = random.randint(1, winy-(squareSize-1))
				for i in range(int(len(squareList)/2)):
					squareList.append([squareList[-1][0],squareList[-1][1]])
				if sleepTime > 0.0:
					sleepTime -= 0.01
			
			
		for i in range(1, len(squareList)):
			tempX = squareList[i][0]
			tempY = squareList[i][1]
			
			if squareList[i][0] == previousX and squareList[i][0] == previousY:
				continue
			squareList[i][0] = previousX
			squareList[i][1] = previousY
			
			previousX = tempX
			previousY = tempY
			
		# Input
		event = pygame.event.get()
		for e in event:
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_UP and direction != 1:
					direction = 0
				if e.key == pygame.K_DOWN and direction != 0:
					direction = 1
				if e.key == pygame.K_LEFT and direction != 3:
					direction = 2
				if e.key == pygame.K_RIGHT and direction != 2:
					direction = 3
				if e.key == pygame.K_ESCAPE:
					done = True
					
		# Draw		
		if retroMode:
			screen.fill((random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)))
			pygame.draw.rect(screen, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (int(foodX), int(foodY), squareSize, squareSize))
			for sq in squareList:
				if direction == 0: # up
					pygame.draw.rect(screen, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (int(sq[0]),int(sq[1]), squareSize, squareSize))
				elif direction == 1: # down            
					pygame.draw.rect(screen, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (int(sq[0]),int(sq[1]), squareSize, squareSize))
				elif direction == 2: # left            
					pygame.draw.rect(screen, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (int(sq[0]),int(sq[1]), squareSize, squareSize))
				else: #right                           
					pygame.draw.rect(screen, (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)), (int(sq[0]),int(sq[1]), squareSize, squareSize))
		else:
			screen.fill((0,0,0))
			pygame.draw.rect(screen, food_color, (int(foodX), int(foodY), squareSize, squareSize))
			for sq in squareList:
				if direction == 0: # up
					pygame.draw.rect(screen, snake_color, (int(sq[0]),int(sq[1]), squareSize, squareSize))
				elif direction == 1: # down            
					pygame.draw.rect(screen, snake_color, (int(sq[0]),int(sq[1]), squareSize, squareSize))
				elif direction == 2: # left            
					pygame.draw.rect(screen, snake_color, (int(sq[0]),int(sq[1]), squareSize, squareSize))
				else: #right                           
					pygame.draw.rect(screen, snake_color, (int(sq[0]),int(sq[1]), squareSize, squareSize))

		
		pygame.display.flip()
		
		time.sleep(sleepTime)

	pygame.display.quit()

if __name__=='__main__':
	main()
