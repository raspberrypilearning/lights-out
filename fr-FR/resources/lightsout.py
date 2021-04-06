import explorerhat
from time import sleep
from time import time 
import random

# La fonction button_pressed
def button_pressed(channel, event):
    
    print("Tu as appuyé sur le bouton "+str(channel) )

    if light == channel:
        print("Bien joué")
    else:
        print("Mauvais bouton !")
        global game_in_progress
        game_in_progress = False
    
    explorerhat.light.off()
    
    global waiting_for_press
    waiting_for_press = False
    


# Continue à jouer au jeu jusqu'à ce que game_in_progress devienne False
game_in_progress = True
TIME_ALLOWED = 1.5

while game_in_progress:
    
    # Choisis au hasard une lumière
    light = random.randint(1,4)

    # Choisis le temps d'attente avant d'allumer la lumière
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


    # Enregistre l'heure actuelle
    start = time()

    waiting_for_press = True
    while waiting_for_press and game_in_progress:

        # Quelle heure est-il maintenant ?
        now = time()
        time_taken = now - start

        if time_taken > TIME_ALLOWED:
            print("Tu as pris trop de temps !")
            explorerhat.light.off()
            game_in_progress = False
            
        else:            
            # Lorsqu'un bouton est appuyé, appelle la fonction button_pressed
            explorerhat.touch.pressed(button_pressed)

