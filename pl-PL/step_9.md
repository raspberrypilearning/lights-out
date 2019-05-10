## Adding a timer

After you switch a light on, you need to start a timer and check how long the player takes to press the button.

- Firstly, you will need to tell Python to import the time function. Next to your other `import` statements, add the line `from time import time` to tell Python you want to use the `time` function.

- Go to the place in your program just before the line of code checking for the button being pressed. Create a variable called `start` to record the current time: this will be provided by your Raspberry Pi and is pretty accurate.
    
    ```python
    # ...other code above
    
    # Record the current time
    start = time()
    
    # ... other code below
    
    ```

- You can choose how many seconds the player will have to press the button once a light is turned on. Add a **constant** to your program just after the `game_in_progress` variable with the value you have chosen. We chose to allow our player 1.5 seconds:
    
    ```python
    game_in_progress = True
    TIME_ALLOWED = 1.5
    
    ```
    
    The smaller the number, the quicker the player will have to be!

- Now add a loop to keep checking whether the user has run over the amount of time they were allowed to take. You can think of this loop's constant checking as being like someone on a long car journey who keeps asking "are we nearly there yet?", "are we there now?", "how about now?"!
    
    ```python
    ...
    
    # Record the current time
    start = time()
    
    waiting_for_press = True
    while waiting_for_press and game_in_progress:
    
        # What's the time now?
        now = time()
        time_taken = now - start
    
        # Check if they have taken more time than they were allowed
        if time_taken > TIME_ALLOWED:
            print("You took too long!")
            explorerhat.light.off()
            game_in_progress = False    # Lose the game
    
        else:
            explorerhat.touch.pressed(button_pressed)
    
    
    ```
    
    Move the code for dealing with button presses to be part of the `else` statement. You will need to **indent** it for it to be in the right place.

- If you run this code you will see that even if you press the correct button extremely quickly, the program will still declare you to have taken too long. This is because you haven't told the game to stop checking if time is up when a button is pressed. Alter your `button_pressed` function to tell the code to stop the timer when a button is pressed.
    
    ```python
        def button_pressed(channel, event):
            print("You pressed " + str(channel) )
    
            explorerhat.light.off()
    
            global waiting_for_press
            waiting_for_press = False
    
    ```
    
    In this code, `global` allows us to change the value of the variable `waiting_for_press` from inside the function.