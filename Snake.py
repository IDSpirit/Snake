import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()

win = pygame.display.set_mode((500, 500))
win.fill((0, 0, 0))

vel = 10
foodLocFound = False
facing = 0
bodyParts = []
font = pygame.font.SysFont('freesansbold.ttf', 25)
facingList = []

class stuff(object):
    def __init__(self, length, x, y, colour):
        self.length = length
        self.x = x
        self.y = y
        self.colour = colour

    def draw(self):
        pygame.draw.rect(win, self.colour, (self.x, self.y, 20, 20))
        #pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, 20, 20), 2)

    def body(self):
        if facing == "l":
            bodyParts.append(stuff(1, self.x + 20, self.y, self.colour))
        elif facing == "r":
            bodyParts.append(stuff(1, self.x - 20, self.y, self.colour))
        elif facing == "u":
            bodyParts.append(stuff(1, self.x, self.y + 20, self.colour))
        elif facing == "d":
            bodyParts.append(stuff(1, self.x, self.y - 20, self.colour))

snakeBody = stuff(0, 100, 100, (255, 255, 255))


def redrawGameWindow():
    global foodLocFound
    global food1
    global food2
    global bodyParts
    
    win.fill((0, 0, 0))
    
    score = font.render(str(snakeBody.length), True, (255, 0, 0))
    win.blit(score, (10, 10))
    
    rand1 = random.randint(0, 480)
    rand2 = random.randint(0, 480)
    #print(foodLocFound)
    if foodLocFound == False:
        while win.get_at((rand1, rand2)) == (255, 255, 255):
            #print("1")
            rand1 = random.randint(0, 480)
            rand2 = random.randint(0, 480)
        #print("2")
        food1 = rand1
        food2 = rand2
        foodLocFound = True
    else:
        #print("3")
        if (snakeBody.x + 20) > food1 and snakeBody.x < (food1 + 20):
            if (snakeBody.y + 20) > food2 and snakeBody.y < (food2 + 20):
                foodLocFound = False
                snakeBody.length = snakeBody.length + 1
                snakeBody.body()
                redrawGameWindow()
        
        food = stuff(1, food1, food2, (255, 0, 0))
        food.draw()
    snakeBody.draw()
    for b in bodyParts[::-1]:
        if b == bodyParts[0]:
            b.x = snakeBody.x
            b.y = snakeBody.y
            #print("a")
        else:
            b.x = bodyParts[(bodyParts.index(b) - 1)].x
            b.y = bodyParts[(bodyParts.index(b) - 1)].y
            #print("b")
##        if facing == "l":
##            b.x = b.x + 15
##        elif facing == "r":
##            b.x = b.x - 15
##        elif facing == "u":
##            b.y = b.y + 15
##        elif facing == "d":
##            b.y = b.y - 15
        b.draw()
    pygame.display.update()

run = True

while run:
    clock.tick(30)

    for event in pygame.event.get(): #ALWAYS INCLUDE THIS AT START OF EVERY PROGRAM
        if event.type == pygame.QUIT:
            run = False 

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        #snakeBody.x = snakeBody.x - vel
        facing = "l"
    elif keys[pygame.K_RIGHT]:
        #snakeBody.x = snakeBody.x + vel
        facing = "r"
    elif keys[pygame.K_UP]:
        #snakeBody.y = snakeBody.y - vel
        facing = "u"
    elif keys[pygame.K_DOWN]:
        #snakeBody.y = snakeBody.y + vel

        #for b in bodyParts:
         #   b.y = b.y + vel
        facing = "d"
    
    if facing == "l" and facingList[-1] != "r": #and snakeBody.x > 0:
        if win.get_at((snakeBody.x - vel, snakeBody.y)) != (255, 255, 255):
            snakeBody.x = snakeBody.x - vel
        else:
            run = False
    elif facing == "r" and facingList[-1] != "l": #and snakeBody.x < (500 - 20):
        if win.get_at((snakeBody.x + 2 * vel, snakeBody.y)) != (255, 255, 255):
            snakeBody.x = snakeBody.x + vel
        else:
            run = False
    elif facing == "u" and facingList[-1] != "d": #and snakeBody.y > 0:
        if win.get_at((snakeBody.x, snakeBody.y - vel)) != (255, 255, 255):
            snakeBody.y = snakeBody.y - vel
        else:
            run = False
    elif facing == "d" and facingList[-1] != "u": #and snakeBody.y < (500 - 20):
        if win.get_at((snakeBody.x, snakeBody.y + 2 * vel)) != (255, 255, 255):
            snakeBody.y = snakeBody.y + vel
        else:
            run = False

    if snakeBody.x >= 500 - 20 or snakeBody.x <= 0 or snakeBody.y <= 0 or snakeBody.y >= 500 - 20:
        run = False

    facingList.append(facing)
    #print(facingList[-1])
    redrawGameWindow()

text = font.render(str("You Lost! Your final score was:  " + str(snakeBody.length)), True, (255, 0, 0))
win.blit(text, (10, 250))
pygame.display.update()
time.sleep(3)

pygame.quit()
