## खूप सारे दिवे!

- आपला प्रोग्रॅम अनियमितरित्या एखादा दिवा निवडून तो चालू करू शकतो, आणि मग बटण दाबल्यावर तो बंद करू शकतो. व्हेरिएबल `game_in_progress` आणि एक लूप तुमच्या खेळामध्ये जोडा जेणेकरून दिवे अनियमितरित्या निवडले जातील.
    
    तुमचा कोड आतापर्यंत असा दिसला पाहिजे:
    
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
    
    लक्षात घ्या की याक्षणी **any (कुठलेही)** बटण दिवे बंद करेल, ते बटण प्रकाशाच्या संख्येशी संबंधित आहे की नाही! हे तितकसं बरोबर नाही परंतु आपण ते नंतर ठीक करू.
    
    ![कोणतेही बटण दाबून तुम्ही दिवे बंद करू शकता](images/press-wrong-button.png)