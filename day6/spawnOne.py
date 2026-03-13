#Import pygame module
import pygame
from pygame.locals import *
import random

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
playerSprite = pygame.image.load("../sprites/dude.png")

#Player state           X   Y
player = { "Position":[10, 10], "Sprite":playerSprite, "Speed":10 }

# Store the obstacles in a list
obstacles = [Rect(100, 0, 10, 200), Rect(250, 180, 100, 100), Rect(400, 380, 200, 10)]

#game window
screen = pygame.display.set_mode([width, height])

#Holds the current direction(s) the player is moving.  Set to no movement
#       left-a right-d up-w  down-s
keys = { K_a:0, K_d:0, K_w:0, K_s:0 }

#keeps time for game
gameClock = pygame.time.Clock()

gameActive = True

enemyLocations = []
spawnLocaion = [640, 240]
enemySpeed = 5

#Main Game loop.  The game runs until the user quits
while gameActive:

    #Limit to 60 FPS
    gameClock.tick(60)

    #Fill screen with bg color
    screen.fill(GREEN)

    # Draw the player image on the screen
    screen.blit(player["Sprite"], player["Position"])
    
    # Draw the obstacles
    for ob in obstacles:
        pygame.draw.rect(screen, ORANGE, ob)

    # Draw Enemies by looping over the list of their locations
    # and draw a 10 by 10 red rectangle at each location
    for enemy in enemyLocations:
        pygame.draw.rect(screen, "red", [enemy[X], enemy[Y], 10, 10])
    
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
    updatedX = player["Position"][X] + xMovement
    updatedY = player["Position"][Y] + yMovement

    # Detect if the updated position intersects with any obstacles
    updatedPlayerRect = Rect(updatedX, updatedY, player["Sprite"].get_width(), player["Sprite"].get_height())
    intersectsObstacles = updatedPlayerRect.collidelist(obstacles) != -1

    #Update player position if new position is in bounds and does not intersect with an obstacle
    if not intersectsObstacles and updatedX >= 0 and updatedX + player["Sprite"].get_width() <= width:
        player["Position"][X] = updatedX
    if not intersectsObstacles and updatedY >= 0 and updatedY + player["Sprite"].get_height() <= height:
        player["Position"][Y] = updatedY

    # Move enemies to follow the player
    for enemy in enemyLocations:
        
        # Determine line of sight by drawing line between
        # enemy and player then test if it intersects with any obstacles
        enemyRect = Rect(enemy[X], enemy[Y], 10, 10)
        hasLineOfSight = True
        for ob in obstacles:
            if ob.clipline(enemyRect.center, updatedPlayerRect.center):
                hasLineOfSight = False
                break
        
        # if the enemy cannot see the player do not move it towards the player
        if not hasLineOfSight:
            continue

        # Move X
        if player["Position"][X] < enemy[X]:
            enemy[X] -= enemySpeed
        elif player["Position"][X] > enemy[X]:
            enemy[X] += enemySpeed
        # Move Y
        if player["Position"][Y] < enemy[Y]:
            enemy[Y] -= enemySpeed
        elif player["Position"][Y] > enemy[Y]:
            enemy[Y] += enemySpeed

    # Spawn new enemies
    randval = random.randrange(60)
    if randval == 7:
        enemyLocations.append(spawnLocaion.copy())

#end pygame
pygame.quit()
