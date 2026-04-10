import pygame

# [levelString] - String representing the level in the format: 2___4445__3: 
# # _ = empty space, widthSize pixels
# # [1-9] = obstacle height 1-9, Generates rectangle with width = widthSize, height = input height * heightSize
# [start] - Starting offset for the obstacles
# [widthSize] - width each character represents in pixels
# [heightSize] - height in pixels of 1 unit of obstacle height
# [groundLevel] - level where obstacle rectangles will be drawn
def generateObstacles(levelString, start, widthSize, heightSize, groundLevel):
    obstacles = []
    distance = start
    for char in levelString:
        if char.isdigit():
            height = int(char) * heightSize
            obstacles.append(pygame.Rect(distance, groundLevel - height, widthSize, height))
            distance += widthSize
        elif char == '_':
            distance += widthSize
        else:
            print("Invalid character in level string: ", char)
    
    return obstacles
