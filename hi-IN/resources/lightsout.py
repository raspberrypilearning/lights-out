import explorerhat
from time import sleep
from time import time 
import random

# बटन_प्रेस्ड फ़ंक्शन
def button_pressed(channel, event):
    
    print("You pressed button "+str(channel) )

    if light == channel:
        print("Well done")
    else:
        print("Wrong button!")
        global game_in_progress
        game_in_progress = False
    
    explorerhat.light.off()
    
    global waiting_for_press
    waiting_for_press = False
    


# गेम तब तक खेलते रहें जब तक game_in_progress फाल्स न हो जाए
game_in_progress = True
TIME_ALLOWED = 1.5

while game_in_progress:
    
    # बिना सोचे समझे एक लाइट चुनें
    light = random.randint(1,4)

    # ये चुनें की लाइट को चालू करने से पहले कितनी देर रुकना है
    wait_for_next = random.uniform(0.5, 3.5)
    sleep(wait_for_next)

    # चुनी हुई लाइट चालू करें
    if light == 1:
        explorerhat.light.blue.on()
    elif light == 2:
        explorerhat.light.yellow.on()
    elif light == 3:
        explorerhat.light.red.on()
    elif light == 4:
        explorerhat.light.green.on()


    # मौजूदा समय रिकॉर्ड करें
    start = time()

    waiting_for_press = True
    while waiting_for_press and game_in_progress:

        # अभी समय क्या है?
        now = time()
        time_taken = now - start

        if time_taken > TIME_ALLOWED:
            print("You took too long!")
            explorerhat.light.off()
            game_in_progress = False
            
        else:            
            # जब एक बटन दबाया जाता है, तो button_pressed फ़ंक्शन को बुलाये
            explorerhat.touch.pressed(button_pressed)

