## टाइमर जोडणे

तुम्ही दिवा चालू केल्यानंतर, तुम्हाला टाइमर सुरु करावा लागेल आणि खेळाडूला बटण दाबण्यास किती वेळ लागतो हे तपासावं लागेल.

- प्रथम, आपल्याला Pythonला टाइम फंक्शन इम्पोर्ट करण्यास सांगण्याची आवश्यकता असेल. आपल्या इतर `import` विधानाशेजारी, `from time import time` Pythonला हे सांगण्यासाठी ही ओळ जोडा की आपल्याला `time` फंक्शन वापरायचे आहे.

- आपल्या प्रोग्रॅम च्या थोडा आधीच्या जागी पोहचा जिथे कोडची ती ओळ आहे जी बटण दाबले जात आहे हे तपासते. वर्तमान (आताची) वेळ रेकॉर्ड करण्यासाठी `start` नावाचे व्हेरिएबल तयार करा: हे आपल्या Raspberry Pi कडून दिले जाईल आणि ते बरेचसे बरोबर आहे.
    
    ```python
    # ...other code above
    
    # Record the current time
    start = time()
    
    # ... other code below
    
    ```

- एकदा दिवा चालू झाला की खेळाडूला किती सेकंद बटण दाबावे लागेल ते आपण निवडू शकता. आपल्‍या प्रोग्राम मध्ये **constant** व्हेरिएबल `game_in_progress` च्या लगेच नंतर आपण निवडलेल मूल्य जोडा. आम्ही आमच्या खेळाडूला 1.5 सेकंद परवानगी देणे निवडले:
    
    ```python
    game_in_progress = True
    TIME_ALLOWED = 1.5
    
    ```
    
    संख्या जितकी लहान असेल तितका खेळाडूला वेगवान व्हाव लागेल!

- आता एक लूप जोडा जे सतत हे तपासत राहील की खेळाडूने दिलेल्या अवधी पेक्षा जास्त वेळ घेतला आहे का नाही. आपण या लूपच्या सततच्या तपासणीबद्दल असा विचार करू शकतो की एखादा गाडीच्या लांबच्या प्रवासाला निघालेला असे विचारत आहे की "आपण जवळपास आलोत का?", "आता आपण तिथे आहोत का?", "आता कुठे?"!
    
    ```python
    ...
    
    # Record the current time
    start = time()
    
    waiting_for_press = True
    while waiting_for_press and game_in_progress:
    
        # What's the time now?
        now = time()
        time_taken = now - start
    
        # Check if they have taken more time than they were allowed
        if time_taken > TIME_ALLOWED:
            print("You took too long!")
            explorerhat.light.off()
            game_in_progress = False    # Lose the game
    
        else:
            explorerhat.touch.pressed(button_pressed)
    
    
    ```
    
    बटण दाबण्यासंदर्भातला कोड `else` विधानाचा भाग होण्यासाठी हलवा. ते योग्य ठिकाणी असण्यासाठी तुम्हाला त्याला **इंडेंट (indent)** करावे लागेल.

- आपण हा कोड चालविल्यास आपल्या लक्षात येईल की आपण बरोबर बटण पटकन दाबले तरीही प्रोग्राम आपल्याला बराच वेळ घेतल्याचे जाहीर करेल. याचे कारण हे आहे की आपण खेळाला बटण दाबल्यास वेळ संपत आहे की नाही हे तपासण्याचे थांबायला सांगितले नाही. आपले `button_pressed` फंक्शन बदला जेणेकरून कोड टाइमरला बटण दाबल्यावर थांबवेल.
    
    ```python
        def button_pressed(channel, event):
            print("You pressed " + str(channel) )
    
            explorerhat.light.off()
    
            global waiting_for_press
            waiting_for_press = False
    
    ```
    
    या कोडमध्ये `global` आम्हाला व्हेरिएबल `waiting_for_press` चे मूल्य फंक्शनच्या आतून बदलू देते.