## Beaucoup de lumières !

- Ton programme peut choisir et allumer une lumière aléatoire, puis l'éteindre quand on appuie sur un bouton. Ajoute une variable `game_in_progress` et une boucle à ton jeu afin que les lumières soient choisies aléatoirement.
    
    Ton code devrait ressembler à ceci :
    
    ```python
    import explorerhat
    from time import sleep
    import random
    
    # button_pressed function
    def button_pressed(channel, event):
        print("Tu as appuyé " + str(channel) )
        explorerhat.light.off()
    
    # Continue à jouer le jeu jusqu'à ce que game_in_progress devienne False
    game_in_progress = True
    
    while game_in_progress:
    
        # Choisis aléatoirement le numéro de la lumière (1-4)
        light = random.randint(1, 4)
    
        # Choisis le temps d'attente avant d'allumer la lumière.
        wait_for_next = random.uniform(0.5, 3.5)
        sleep(wait_for_next)
    
        # Allume la lumière sélectionnée
        if light == 1:
            explorerhat.light.blue.on()
        elif light == 2:
            explorerhat.light.yellow.on()
        elif light == 3:
            explorerhat.light.red.on()
        elif light == 4:
            explorerhat.light.green.on()
    
        # Lorsqu'un bouton est appuyé, appeler la fonction button_pressed
        explorerhat.touch.pressed(button_pressed)
    
    ```
    
    Note qu'au moment d'appuyer sur **n'importe quel** bouton éteindra la lumière, que ce bouton corresponde ou non au numéro de la lumière ! Ce n'est pas tout à fait juste, mais nous le corrigerons plus tard.
    
    ![Tu peux appuyer sur n'importe quel bouton pour éteindre la lumière](images/press-wrong-button.png)