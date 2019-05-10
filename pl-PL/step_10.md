## But was it the right button?

The final part of our game is to check if the button the player pressed was in fact the right button. To do this you need to edit your `button_pressed` function again. At the start of the function, add code to check whether the variable `light` (the number of the chosen light) is equal to the variable `channel` (the number of the button pressed):

```python
def button_pressed(channel, event):
    if light == channel:
        print("Well done")
    else:
        print("Wrong button")
        global game_in_progress
        game_in_progress = False
```

Once again, you will need to tell Python that you want to change the value of the variable `game_in_progress` from inside the function by using the word `global`.

![The game should now detect whether the right button was pressed](images/press-right-button.png)

That's it! Now test your game with your friends.