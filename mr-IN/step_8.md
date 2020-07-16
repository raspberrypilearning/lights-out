## Lots of lights!

- Your program can choose and switch on a random light, and then switch it off when a button is pressed. Add a `game_in_progress` variable and a loop to your game so that lights keep being randomly chosen.
    
    Your code so far should look like this:
    
    ```python
    import explorerhat
    from time import sleep
    import random
    
    # The button_pressed function
    def button_pressed(channel, event):
        print("You pressed " + str(channel) )
        explorerhat.light.off()
    
    # Keep playing the game until game_in_progress becomes False
    game_in_progress = True
    
    while game_in_progress:
    
        # Randomly choose the number of a light (1-4)
        light = random.randint(1, 4)
    
        # Choose how long to wait before turning on the light
        wait_for_next = random.uniform(0.5, 3.5)
        sleep(wait_for_next)
    
        # Turn on the selected light
        if light == 1:
            explorerhat.light.blue.on()
        elif light == 2:
            explorerhat.light.yellow.on()
        elif light == 3:
            explorerhat.light.red.on()
        elif light == 4:
            explorerhat.light.green.on()
    
        # When a button is pressed, call the button_pressed function
        explorerhat.touch.pressed(button_pressed)
    
    ```
    
    Notice that at the moment pressing **any** button will turn the light off, whether that button corresponds to the light's number or not! That's not quite right but we will fix it later.
    
    ![You can press any button to turn the light off](images/press-wrong-button.png)