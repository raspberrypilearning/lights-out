## Veel lampjes!

- Je programma kan een willekeurig lampje kiezen en inschakelen en vervolgens uitschakelen wanneer een knop wordt ingedrukt. Voeg een `game_in_progress` variabele en een lus toe aan je spel, zodat de lichten willekeurig worden gekozen.
    
    Je code tot nu toe zou er als volgt uit moeten zien:
    
    ```python
    import explorerhat
    from time import sleep
    import random
    
    # The button_pressed function
    def button_pressed(channel, event):
        print("Je drukte op knop " + str(channel) )
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
    
    Merk op dat als een  **willekeurige** knop gedrukt wordt het licht uitgaat, of die knop overeenkomt met het nummer of niet! Dat klopt niet helemaal, maar we zullen het later oplossen.
    
    ![Je kunt op een willekeurige knop drukken om het licht uit te schakelen](images/press-wrong-button.png)