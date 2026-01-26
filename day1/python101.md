# Introduction to Python

During this internship we will use python and the python library pygame to build a video game.  Each week we will review a few python or pygame concepts and you will learn more by building your game.

> If you want to learn using a more traditional course try the [Python course at Khan Academy](https://www.khanacademy.org/computing/intro-to-python-fundamentals)


## About Thonny

Open the Thonny app by clicking Berry->Programming 

The main text area is where you can write code and the 'Shell' below is where the code is executed.

## Run your first code

In the text window enter the following code and press the green play button to run the code.

```python
print("Hello World")
```

Congratulations, you have run your first python code!  

> Try to write a new line using the print function to print out something else.

### Math

Math is used a lot when making video games, luckily python can do the math for you.

To see python doing math for you write an equation inside of the print function.

```python
print(6 * 7)
```

Press the green play button to run the code.

Try to write your own equation.

> For a list of all arithmetic operators see [Python docs](https://www.w3schools.com/python/gloss_python_arithmetic_operators.asp)

### Variables

You can store the result of a math operation or anything else you do in a variable so you can use it later.

```python
theAnswer = 6 * 7
print(theAnswer)
```

This does the same thing as `print(6 * 7)` but it stores the result of the math operation so it can be used later

### Comments

Comments are just there to help humans understand the code.  The code behaves the same with or with out them.

```python
theAnswer = 6 * 7  # The answer is 42!
print(theAnswer)
```


## Create your first pygame code

Pygame is a library, to use it we must import it into our code.  Then we can call functions from pygame to create a game.

### Create a game window

```python
# Import pygame
import pygame

# Initialize the pygame
pygame.init()

# Create Variables for size of the game screen
width = 640
height = 480

# Create game window
screen = pygame.display.set_mode([width, height])

# Make the game window green
screen.fill('green')

# Draw the game window
pygame.display.flip()
```

> Try changing the color of the screen.

### Draw shapes

For documentation on how to draw shapes see pygame's [draw docs](https://www.pygame.org/docs/ref/draw.html)


```python
# draw a circle
pygame.draw.circle(screen, "orange", [200, 200], 40)
```

> Try to create another shape, put this one in a different location or change it's size.

### Create a game loop

A loop runs code contained within it until the loop exits.  For our video games we will have a loop that runs until the game is over.  The loop runs once for every frame so contains the code necessary to draw a single frame.

```python
# Import pygame
import pygame

# Initialize the pygame
pygame.init()

# Create Variables for size of the game screen
width = 640
height = 480

# Create game window
screen = pygame.display.set_mode([width, height])

while True:
    # Make the game window green
    screen.fill('green')

    # draw a circle
    pygame.draw.circle(screen, "orange", [200, 200], 40)

    # Draw the game window
    pygame.display.flip()
```

When you run this program nothing moves.  Has adding the game loop changed anything?  How could we use the game loop to make things change on screen each turn?