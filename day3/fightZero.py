#Import pygame module
import pygame
from pygame.locals import *

#Initialize the pygame
pygame.init()

####constants####
#Colors
GREEN = (0, 168, 42) 
ORANGE = (255, 102, 0) 
#Accessors
X = 0
Y = 1
#game window size
width = 640
height = 480

####game variables####
playerSprite = pygame.image.load("dude.png")

#Player state           X   Y
player = { "Position":[10, 10], "Sprite":playerSprite, "Speed":10 }

groundLevel = 400

gravity = 1
fallSpeed = 0

#game window
screen = pygame.display.set_mode([width, height])

#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = { K_a:0, K_d:0, K_w:0, K_s:0 }

#keeps time for game
gameClock = pygame.time.Clock()

gameActive = True

#Main Game loop.  The game runs until the user quits
while gameActive:

    #Limit to 60 FPS
    gameClock.tick(60)

    #Fill screen with bg color
    screen.fill(GREEN)

    # Draw ground
    pygame.draw.rect(screen, ORANGE, [0, groundLevel, width, height - groundLevel])

    # Draw the player image on the screen
    screen.blit(player["Sprite"], player["Position"])
    
    #Draw arena (surface)
    pygame.display.update()

    ##Loop over input to see if the keys w, s, a or d were pressed or released
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:            #A key was pressed
            keys[event.key] = player["Speed"]
        elif event.type == pygame.KEYUP:            #A key was released
            keys[event.key] = 0
        elif event.type == pygame.QUIT:             #The user quit
            gameActive = False

    #Determine new player position based on keyboard input
    xMovement = keys[K_d] - keys[K_a]
    yMovement = keys[K_s] - keys[K_w]
    if player["Position"][Y] + player["Sprite"].get_height() < groundLevel:
        fallSpeed += gravity
        print("fallSpeed: ", fallSpeed)
    else:
        fallSpeed = 0
    updatedX = player["Position"][X] + xMovement
    updatedY = player["Position"][Y] + yMovement + fallSpeed

    #Update player position if new position is in bounds
    if updatedX >= 0 and updatedX + player["Sprite"].get_width() <= width:
        player["Position"][X] = updatedX
    if updatedY >= 0 and updatedY + player["Sprite"].get_height() <= groundLevel:
        player["Position"][Y] = updatedY
    if updatedY + player["Sprite"].get_height() > groundLevel:
        player["Position"][Y] = groundLevel - player["Sprite"].get_height()
    

#end pygame
pygame.quit()
