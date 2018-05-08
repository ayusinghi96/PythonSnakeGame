import pygame, time, random


x = pygame.init()
##print(x)
##this displays(6,0)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_x = 600
display_y = 400

gameDisplay = pygame.display.set_mode((display_x,display_y))
pygame.display.set_caption('Snake')
## concept of flip and update both are same just the difference is that update only updates required fields and flip will refresh entire page.
#pygame.display.flip()

pygame.display.update()

img = pygame.image.load('snakehead.png')
img2 = pygame.image.load('apple.png')

icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

appleThickness = 30
block_size = 20
FPS = 10

direction = "right"


smallfont = pygame.font.SysFont("comicsansms", 15)
medfont = pygame.font.SysFont("comicsansms", 20)
largefont = pygame.font.SysFont("comicsansms", 60)
## this a general msg function that can be used to deliver messages on the screen

def pause():
    paused = True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.fill(black)
        message_to_screen("paused", white, -20, "large")
        message_to_screen("Press C to continue or Q to Quit", white, 50, "small")

        pygame.display.update()
        clock.tick(5)


def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])

def randApple():
     randAppleX = round(random.randrange(0,display_x-appleThickness))#/10.0)*10.0
     randAppleY = round(random.randrange(0,display_y-appleThickness))#/10.0)*10.0

     return randAppleX, randAppleY


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        
        
        gameDisplay.fill(black)
        message_to_screen("Welcome to SNAKE", green, -60, "large")
        message_to_screen("Eat red apples and earn points", white, 0, "small")
        message_to_screen("Eat as many apples  as you can and get long", white, +20, "small")
        message_to_screen("If you run into yourself or run into boundary you die", white, +40, "small")
        
        message_to_screen("Press C to Play or Q to Exit or P to Pause", red, +90, "medium")

        pygame.display.update()
        clock.tick(15)


def snake(block_size, snakeList):
    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0],XnY[1],block_size,block_size])    

def text_objects(text, color, size):
    global textSurface
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)

        
    return textSurface, textSurface.get_rect()
    

def message_to_screen(msg, color, y_displace = 0, size = "size"):
    textSurf, textRect = text_objects(msg,color, size)
##    screen_text = font.render(msg, True, color)
##    gameDisplay.blit(screen_text, [display_x/2, display_y/2])
    textRect.center = (display_x / 2), (display_y / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)

    

def gameLoop():
    global direction

    direction = 'right'
    gameExit = False
    gameOver = False
    
    lead_x = display_x/2
    lead_y = display_y/2
    
    lead_x_change = 15
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    
##    randAppleX = round(random.randrange(0,display_x-appleThickness))#/10.0)*10.0
##    randAppleY = round(random.randrange(0,display_y-appleThickness))#/10.0)*10.0
    randAppleX, randAppleY = randApple()

    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game Over!", red, -50, "large")
            message_to_screen("Press C to play again and Q to Quit", white, 50, "medium")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                    
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                        
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
    ##        print(event)
    ##        this prints all the value of all the events(mouse hovering, keypress, keyrelease, mouse click) in the log
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

    ##  Chexking for collision with the window boundries
        if lead_x >= display_x or lead_x < 0 or lead_y >= display_y or lead_y < 0:
            gameOver = True
                

                    
    ## This block of code is used when we want that motion continues for long press of arrow keys
            
    ##        if event.type == pygame.KEYUP:
    ##            if event.key == pygame.K_LEFT or pygame.K_RIGHT:
    ##                lead_x_change = 0

                    
                    
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        
##        pygame.draw.rect(gameDisplay, red,[randAppleX, randAppleY, appleThickness, appleThickness])
        gameDisplay.blit(img2, (randAppleX, randAppleY))
        

 
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(block_size,snakeList)

        score(snakeLength - 1)
    ##    drawing objects on the display screen
        
    ##    pygame.draw.rect(gameDisplay, red, [400,300,50,10])
        
    ##    another method of doing so
    ##    gameDisplay.fill(red,rect = [200,200,100,10])

        pygame.display.update()
        
# colission of snake and apple of same size just checking for origin points(top left corner) of both apple and snake head:          
##        if lead_x == randAppleX and lead_y == randAppleY:
##            randAppleX = round(random.randrange(0,display_x-block_size)/10.0)*10.0
##            randAppleY = round(random.randrange(0,display_y-block_size)/10.0)*10.0
##            snakeLength += 1


# colission of snake and apple of same size (checking if the topp left corner of the snake head lies in between the dimensions of the apple):          
##        if lead_x >= randAppleX and lead_x < randAppleX + appleThickness:
##            if lead_y >= randAppleY and lead_y < randAppleY + appleThickness:
##                randAppleX = round(random.randrange(0,display_x-block_size))#/10.0)*10.0
##                randAppleY = round(random.randrange(0,display_y-block_size))#/10.0)*10.0
##                snakeLength += 1


# colission of snake and apple of diferent sizes(checing if any dimension of the snake comes in the region enclosed by the apple):        
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThickness:

            if lead_y > randAppleY and lead_y < randAppleY + appleThickness:
                randAppleX, randAppleY = randApple()
                snakeLength += 1
                
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThickness:
                randAppleX, randAppleY = randApple()
                snakeLength += 1
        
        clock.tick(FPS)

##    message to be displayed on the screen on exit
        
##    message_to_screen("You Lose", red)
##    pygame.display.update()
##    this is used to keep font on the screen. if sleep is not used then the text will only flash ones and get removed on refresh
##    time.sleep(FPS)
    pygame.quit()
    quit()

game_intro()
gameLoop()
