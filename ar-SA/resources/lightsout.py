import explorerhat
from time import sleep
from time import time 
import random

# دالة button_pressed
def button_pressed(channel, event):
    
    print("قمت بالضغط على زر"+str(channel) )

    if light == channel:
        print("احسنت")
    else:
        print("الزر خطأ!")
        global game_in_progress
        game_in_progress = False
    
    explorerhat.light.off()
    
    global waiting_for_press
    waiting_for_press = False
    


# استمر في لعب اللعبة حتى تصبح game_in_progress = False
game_in_progress = True
TIME_ALLOWED = 1.5

while game_in_progress:
    
    # اختر ضوءاً بشكل عشوائي
    light = random.randint(1,4)

    # اختر مدة الانتظار قبل تشغيل الضوء
    wait_for_next = random.uniform(0.5, 3.5)
    sleep(wait_for_next)

    # قم بتشغيل الضوء المحدد
    if light == 1:
        explorerhat.light.blue.on()
    elif light == 2:
        explorerhat.light.yellow.on()
    elif light == 3:
        explorerhat.light.red.on()
    elif light == 4:
        explorerhat.light.green.on()


    # سجل الوقت الحالي
    start = time()

    waiting_for_press = True
    while waiting_for_press and game_in_progress:

        # ما الوقت الآن؟
        now = time()
        time_taken = now - start

        if time_taken > TIME_ALLOWED:
            print("لقد استغرقت وقتاً طويلاً")
            explorerhat.light.off()
            game_in_progress = False
            
        else:            
            # عند الضغط على زر، استدعِ الدالة button_pressed
            explorerhat.touch.pressed(button_pressed)

