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

# Points defining path player will move along
path = [[320, 480], [320, 400], [200, 400], [200, 300], [400, 200], [400, 0]]

#Player state
player = { "Position":path[0].copy(), "Target": 1, "Sprite":playerSprite, "Speed":10 }

#game window
screen = pygame.display.set_mode([width, height])

#keeps time for game
gameClock = pygame.time.Clock()

gameActive = True

#Main Game loop.  The game runs until the user quits
while gameActive:

    #Limit to 60 FPS
    gameClock.tick(60)

    #Fill screen with bg color
    screen.fill(GREEN)

    # Draw the player image on the screen
    screen.blit(player["Sprite"], player["Position"])
    
    #Draw arena (surface)
    pygame.display.update()

    ##Loop over input to see if the game is quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:             #The user quit
            gameActive = False

    # update the player position to move closer to the target point
    targetPoint = path[player["Target"]]
    # Move X
    if targetPoint[X] < player["Position"][X]:
        player["Position"][X] -= 1
    elif targetPoint[X] > player["Position"][X]:
        player["Position"][X] += 1
    # Move Y
    if targetPoint[Y] < player["Position"][Y]:
        player["Position"][Y] -= 1
    elif targetPoint[Y] > player["Position"][Y]:
        player["Position"][Y] += 1
    
    # if player reaches current target update the target or reset if reached final target
    if targetPoint == player["Position"]:
        print("At Point", player["Target"])
        if player["Target"] < len(path) - 1:
            player["Target"] += 1
            print("Target incremented", player["Target"])
        else:
            player["Target"] = 1
            player["Position"] = path[0]
            print("Target Reset", player["Position"])
    
    

#end pygame
pygame.quit()
