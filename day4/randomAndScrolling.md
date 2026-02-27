# Random and Scrolling



## Random

Random numbers can be generated with the `random` python library.  To use random functions import the random library.

```python
import random
```

The documentation for the [random library](https://docs.python.org/3/library/random.html#functions-for-integers) explains all the functions available.  


### Using random.randrange to spawn enemies at a random time

The following code will generate a random number from 0 to 59, if that number equals 42 it will run the code you add to spawn an enemy.

```python
    randval = random.randrange(60)
    if randval == 42:
        # Spawn enemy
```

> Note 1: Assuming you are running 60 frames per second and equally distributed random values this will spawn an average of one enemy per second.

> Note 2: `random.randint(60)` will generate a random value from 0 to 60 ... 


### Using random.randrange to spawn enemies at a random location

The following code will generate a point at a random location along the right hand side of the screen.  It could be used in enemy spawn code you write.

```python
    width = 640
    height = 480
    spawnLocation = [width, random.randrange(height)]
```

> Note: the width and height variables are defined in this example but your game already has the game window size already defined.  Use those existing variables instead of redefining them


## Scrolling

We can simulate movement by moving the ground and or background across the screen a consistent number of pixels every frame.

A simple example of this is to define a list of rectangles initially positioned off the right edge of the screen then move them every frame.


```python
# ... Initialization Code

# speed objects will move across the screen
groundSpeed = 4

# list of rectangles
obstacles = [Rect(width, groundLevel - 20, 20, 20), 
            Rect(width + 200, groundLevel - 30, 20, 30), 
            Rect(width + 410, groundLevel - 20, 40, 20),
            Rect(width + 780, groundLevel - 40, 20, 40),
            Rect(width + 975, groundLevel - 10, 50, 10)]

# Game Loop
while True:
    # ... Draw 

    # Loop over all obstacles and draw each one
    for ob in obstacles:
        pygame.draw.rect(screen, "brown", ob)
    
    #Draw arena (surface)
    pygame.display.update()

    # ... User input and other game logic

    # Loop over all obstacles and move each one
    for ob in obstacles:
        ob.move_ip(-groundSpeed, 0)

pygame.exit()
```

> Note 1: This example focuses on code used to create and move obstacles and is designed to be added to existing examples.

#### Creating rectangles

Each rectangle is created using the [contructor for the Rect class
](https://www.pygame.org/docs/ref/rect.html)

```python
Rect(left, top, width, height)
```

> Question: In the example code why is the top position set to `groundLevel - height`?

#### Drawning the rectangles

A for loop is used to loop over each rectangle in the `obtacles` list and the [`pygame.draw.rect`](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect) command is used to draw them.

```python
pygame.draw.rect(surface, color, rect)
```

#### Moing the rectangles

A for loop is used to loop over each rectangle in the `obstacles` list and the  [Rect.move_ip](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move_ip) function is used to them

```python
move_ip(x, y)
```

