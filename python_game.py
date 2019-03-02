import os
print os.getcwd()
import pygame
pygame.init()

win = pygame.display.set_mode((500,480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('Game/R1.png'),pygame.image.load('Game/R2.png'),pygame.image.load('Game/R3.png'),pygame.image.load('Game/R4.png'),pygame.image.load('Game/R5.png'),pygame.image.load('Game/R6.png'),pygame.image.load('Game/R7.png'),pygame.image.load('Game/R8.png'),pygame.image.load('Game/R9.png')]

walkLeft = [pygame.image.load('Game/L1.png'),pygame.image.load('Game/L2.png'),pygame.image.load('Game/L3.png'),pygame.image.load('Game/L4.png'),pygame.image.load('Game/L5.png'),pygame.image.load('Game/L6.png'),pygame.image.load('Game/L7.png'),pygame.image.load('Game/L8.png'),pygame.image.load('Game/L9.png')]

bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

x=50
y=400
width=40
height=60
vel=5
isJump = False
jumpCount = 10
run = True
left = False
right = False
walkCount = 0

def redrawGameWindow():
	global walkCount
	win.blit(bg,(0,0))

	if walkCount + 1 >= 27 :
		walkCount = 0
		#print walkCount
	if left :
		win.blit(walkLeft[walkCount//3],(x,y))
		walkCount += 1
		#print walkCount
	elif right :
		win.blit(walkRight[walkCount//3],(x,y))
		walkCount += 1
	else:
		win.blit(char,(x,y))

        #pygame.draw.rect(win,(0,255,0),(x,y,width,height))
        pygame.display.update()
         
	


#mainloop
run = True
while run:
	pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x > vel:
		x -= vel
		left = True
		right = False

	elif keys[pygame.K_RIGHT] and x < 500 - width - vel:
		x += vel
		right = True
		left = False
	
	else:
		right = False
		left = False
		walkCount = 0
	
        if not(isJump):

		if keys[pygame.K_UP] and y > vel:
			y -= vel
	
		if keys[pygame.K_DOWN] and y < 500 - height - vel:
			y += vel
        
        	if keys[pygame.K_SPACE]:
			isJump = True
        else:
		if jumpCount >= -10 :
			neg = 1
			#print(jumpCount)
			if jumpCount < 0:
				neg = -1
            		y -= (jumpCount ** 2) * 0.5 * neg
			#print(y)
			jumpCount -= 1
		else:
			isJump = False
			jumpCount = 10
       
	redrawGameWindow()




pygame.quit()

