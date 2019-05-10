import explorerhat
from time import sleep
from time import time 
import random

# De knop ingedrukt-functie
def button_pressed(channel, event):
    
    print ("Je drukte op de knop" + str (channel))

    if light == channel:
        print ("Goed gedaan")
    else:
        print ("Verkeerde knop!")
        global game_in_progress
        game_in_progress = False
    
    explorerhat.light.off()
    
    global waiting_for_press
    waiting_for_press = False
    


# Blijf het spel spelen totdat game_in_progress False wordt
game_in_progress = True
TIME_ALLOWED = 1.5

while game_in_progress:
    
    # Kies willekeurig een licht
    light = random.randint(1,4)

    # Kies hoe lang je moet wachten voordat het licht aangaat
    wait_for_next = random.uniform(0.5, 3.5)
    sleep(wait_for_next)

    # Schakel het geselecteerde licht in
    if light == 1:
        explorerhat.light.blue.on()
    elif light == 2:
        explorerhat.light.yellow.on()
    elif light == 3:
        explorerhat.light.red.on()
    elif light == 4:
        explorerhat.light.green.on()


    # Neem de huidige tijd
    start = time()

    waiting_for_press = True
    while waiting_for_press and game_in_progress:

        # Wat is nu de tijd?
        now = time()
        time_taken = now - start

        if time_taken > TIME_ALLOWED:
            print ("Het heeft te lang geduurd!")
            explorerhat.light.off()
            game_in_progress = False
            
        else:            
            # Wanneer een knop is ingedrukt, de button_pressed functie aanroepen
            explorerhat.touch.pressed(button_pressed)

