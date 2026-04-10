# Level Generator

Writing out levels by hand is  labor intensive and error prone.  Here is an example from [scrollOne.py](../day5/scrollOne.py) which creates 5 obstacles:

```python
obstacles = [Rect(width, groundLevel - 20, 20, 20), 
            Rect(width + 200, groundLevel - 30, 20, 30), 
            Rect(width + 410, groundLevel - 20, 40, 20),
            Rect(width + 780, groundLevel - 40, 20, 40),
            Rect(width + 970, groundLevel - 10, 50, 10)]
```

This describes a one obstacle 20x20 pixels, then 200 pixels empty space to the next which is 20x30 pixels and so on.

We could represent something similar with a very simple and compact string format where an empty space was represented by an underscore `_` and an obstacle was represented by a number from 1-9 representing the obstacles height:

```python
levelString = "22__________33___________2222________________44__________11111"
```

This is a very simple format because the program can determine what to generate by looking at each individual character.  If there is a digit generate an obstacle, if there is an underscore add some empty space.

## Code concepts

What code concepts are necessary to generate obstacles from the string above?  

To determine it think about what you need to do to read the format.

1. Look at characters one at a time
2. If it is a number create rectangle with the correct size and add it to the list of obstacles
3. If it is an underscore add one space to the offset

What code can we use for each of these steps?

1. for loop over the characters in the levelString.
2. If block that tests if the character currently being inspected is a digit.
3. If block that tests if the character currently being inspected is an underscore.

We also need a variable to store the offset which is incremented one width for each character.  We can use the existing `obstacles` variable to hold the output rectangles.

One final extra concept is to put this logic in a function for clarity and reuse

## Code

### Function

```python
def generateObstacles (levelString, start, widthSize, heightSize, groundLevel):
    obstacles = []
    distance = start

    # ... generation code here

    return obstacles
```

The parameters of this function are:
- **levelString** - String representing the level
- **start** - Starting offset for the obstacles
- **widthSize** - Width each character represents in pixels
- **heightSize** - Height in pixels of one unit of obstacle height
- **groundLevel** - level where obstacles will be drawn

### For loop

```python
    for char in levelString:
```

This for loop runs once for each character in the level string with each character stored in `char` variable.

### Generation code

```python
        if char.isdigit():
            height = int(char) * heightSize
            obstacles.append(pygame.Rect(distance, groundLevel - height, widthSize, height))
            distance += widthSize
        elif char == '_':
            distance += widthSize
        else:
            print("Invalid character in level string: ", char)
```

This code generates levels for digits and underscores and prints out an error if the `levelString` contains anything but digits and underscores.