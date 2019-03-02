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
clock = pygame.time.Clock()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10

    def draw(self , win):
	
	if self.walkCount + 1 >= 27 :
		self.walkCount = 0
		#print walkCount
	if self.left :
		win.blit(walkLeft[self.walkCount//3],(self.x,self.y))
		self.walkCount += 1
		#print walkCount
	elif self.right :
		win.blit(walkRight[self.walkCount//3],(self.x,self.y))
		self.walkCount += 1
	else:
		win.blit(char,(self.x,self.y))
		


def redrawGameWindow():
	global walkCount
	win.blit(bg,(0,0))

	man.draw(win)

        #pygame.draw.rect(win,(0,255,0),(x,y,width,height))
        pygame.display.update()
         
	


#mainloop
man = player(200,410,64,64)
run = True
while run:
	clock.tick(27)
	#pygame.time.delay(100)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and man.x > man.vel:
		man.x -= man.vel
		man.left = True
		man.right = False

	elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
		man.x += man.vel
		man.right = True
		man.left = False
	
	else:
		man.right = False
		man.left = False
		man.walkCount = 0
	
        if not(man.isJump):

		if keys[pygame.K_UP] and man.y > man.vel:
			man.y -= man.vel
	
		if keys[pygame.K_DOWN] and man.y < 500 - man.height - man.vel:
			man.y += man.vel
        
        	if keys[pygame.K_SPACE]:
			man.isJump = True
        else:
		if man.jumpCount >= -10 :
			neg = 1
			#print(jumpCount)
			if man.jumpCount < 0:
				neg = -1
            		man.y -= (man.jumpCount ** 2) * 0.5 * neg
			#print(y)
			man.jumpCount -= 1
		else:
			man.isJump = False
			man.jumpCount = 10
       
	redrawGameWindow()




pygame.quit()

