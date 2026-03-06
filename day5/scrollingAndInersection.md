# Scrolling And Intersection

We can use a modified version of the logic from [day3/intersectZzero.py](../day3/intersectZero.py) to detect if the player intersects with an obstacle and adjust it's position if it does.

`intersectZero.py` has the following code

```python
    # Detect if the updated position intersects with any obstacles
    updatedPlayerRect = Rect(updatedX, updatedY, player["Sprite"].get_width(), player["Sprite"].get_height())
    intersectsObstacles = updatedPlayerRect.collidelist(obstacles) != -1
```

If the player inersects with an obstacle `intersectsObstacles` is set to true.  We need to know if there is an intersection AND which obstacle the player intersects with.  Review the docs for [`Rect.collidelist`](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.collidelist) to see if there is a way we can get both.

Once we know how to get the rectangle the player intersects with we can use a modified version of the code to keep the player inbounds to force it to move around the obstacles.

The starting code is below, we want to focus on the conditions that determine if the `updatedX` or `updatedY` put the player out of bounds or below the ground.

```python
    #Update player position if new position is in bounds
    if updatedX >= 0 and updatedX + player["Sprite"].get_width() <= width:
        player["Position"][X] = updatedX
    if updatedY >= 0 and updatedY + player["Sprite"].get_height() <= groundLevel:
        player["Position"][Y] = updatedY
```

The first condition `updatedX >= 0 and updatedX + player["Sprite"].get_width() <= width` is true if the left side of the player is within the left bounds of the screen and the right side of the player is within the right bounds of the screen.

The second condition `updatedY >= 0 and updatedY + player["Sprite"].get_height() <= groundLevel` is true if the top of the player is within the top bounds of the screen and the bottom of the plyer is above the ground.

What horizontal and vertical conditions do we need to check for when the player interesects with an obstacle?

