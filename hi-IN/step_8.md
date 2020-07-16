## बहुत सारी रोशनी!

- आपका प्रोग्राम रैंडम लाइट चुनकर उसको चालू कर सकता है, और फिर बटन दबाए जाने पर उसे स्विच ऑफ कर सकता है। अपने खेल के लिए एक `game_in_progress` वेरिएबल और लूप जोड़े ताकि रोशनी अनियमित ढंग से चुनी जा सके।
    
    अब तक आपका कोड इस तरह दिखना चाहिए:
    
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
    
    ध्यान दें कि फिलहाल **कोई भी** बटन प्रकाश को बंद कर देगा, चाहे वह बटन प्रकाश की संख्या से मेल खाता हो या नहीं! यह बिलकुल सही नहीं है लेकिन हम इसे बाद में ठीक कर देंगे।
    
    ![लाइट बंद करने के लिए आप कोई भी बटन दबा सकते हैं](images/press-wrong-button.png)