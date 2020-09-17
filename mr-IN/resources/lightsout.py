import explorerhat
from time import sleep
from time import time 
import random

# button_pressed function
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
    


# game_in_progress False होईपर्यंत गेम खेळत रहा
game_in_progress = True
TIME_ALLOWED = 1.5

while game_in_progress:
    
    # सहजगत्या प्रकाश निवडा
    light = random.randint(1,4)

    # लाईट चालू करण्यापूर्वी किती काळ थांबायचे ते निवडा
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


    # वर्तमान वेळ नोंदवा
    start = time()

    waiting_for_press = True
    while waiting_for_press and game_in_progress:

        # आता किती वाजले आहेत?
        now = time()
        time_taken = now - start

        if time_taken > TIME_ALLOWED:
            print("You took too long!")
            explorerhat.light.off()
            game_in_progress = False
            
        else:            
            # जेव्हा एक बटण दाबले जाते तेव्हा बटणावर क्लिक करा
            explorerhat.touch.pressed(button_pressed)

