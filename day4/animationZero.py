import pygame

pygame.init()

catFighter1 = pygame.image.load("sprites/cat_fighter_sprite1.png")
sheet_width = catFighter1.get_width()
sheet_height = catFighter1.get_height()

cat1 = []
row_height = 0
row_width = 0
row = 0
while row_height < sheet_height:
    cat1.append([])
    while row_width < sheet_width:
        catCell = pygame.Surface([50,50], pygame.SRCALPHA, 32)
        catCell.blit(catFighter1, [0,0], [row_width, row_height, 50, 50])
        cat1[row].append(catCell)
        row_width += 50
    row += 1
    row_height += 50
    row_width = 0


print(row)

#game window size
width = 640
height = 480

#game window
screen = pygame.display.set_mode([width, height])

screen.fill("blue")

y = 0
for catRow in cat1:
    x = 0
    print("Row:", y)
    for cat in catRow:
        screen.blit(cat, [x, y])
        x += 55
    y += 55

pygame.display.update()