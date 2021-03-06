## टाइमर(timer) जोड़ना

आपके लाइट ऑन करने के बाद, आपको टाइमर शुरू करने और यह जांचने की आवश्यकता है कि खिलाड़ी को बटन दबाने में कितना समय लगता है।

- सबसे पहले, आपको टाइम फ़ंक्शन को import करने के लिए Python को बताना होगा। अपने अन्य `import` स्टेटमेंट्स के आगे, लाइन `from time import time` जोड़ें Python को बताने के लिए कीआप `time` फंक्शन का उपयोग करना चाहते हैं ।

- अपने प्रोग्राम में बटन दबाए जाने के चेकिंग के लिए कोड की लाइन से ठीक पहली जगह पर जाएं। एक वैरिएबल बनाएं जिसे `start` कहा जाता है, वर्तमान समय रिकॉर्ड करने के लिए: यह आपके Raspberry Pi द्वारा प्रदान किया जाएगा और बहुत सटीक है।
    
    ```python
    # ...other code above
    
    # Record the current time
    start = time()
    
    # ... नीचे अन्य कोड
    
    ```

- लाइट ऑन होने के बाद आप यह चुन सकते हैं कि खिलाड़ी को कितने सेकंड बटन प्रेस करना होगा। अपने कार्यक्रम में `game_in_progress` वेरिएबल के ठीक बाद आपके द्वारा चुने गए मान(value) के साथ एक **constant** जोड़ें । हमने अपने खिलाड़ी को 1.5 सेकंड की अनुमति देना चुना है:
    
    ```python
    game_in_progress = True
    TIME_ALLOWED = 1.5
    
    ```
    
    संख्या जितनी कम होगी, खिलाड़ी उतना ही तेज होगा!

- अब यह जाँचने के लिए कि क्या उपयोगकर्ता ने अनुमति से ज़्यादा समय ले लिया है एक लूप जोड़ें । आप इस लूप की निरंतर जाँच के बारे में सोच सकते हैं जैसे एक लंबी कार यात्रा पर कोई है जो पूछता है कि "क्या हम अभी तक वहाँ हैं?", "क्या हम अभी वहाँ हैं?", "अभी हम कहाँ है?"
    
    ```python
    ...
    
    # टाइम को रिकॉर्ड करना
    start = time()
    
    waiting_for_press = True
    while waiting_for_press and game_in_progress:
    
        # अब क्या टाइम है?
        now = time()
        time_taken = now - start
    
        # ये देखे की क्या उन्होंने ज़्यादा टाइम लगाया जीतन उन्हें मिला था
        if time_taken > TIME_ALLOWED:
            print("You took too long!")
            explorerhat.light.off()
            game_in_progress = False    # Lose the game
    
        else:
            explorerhat.touch.pressed(button_pressed)
    
    
    ```
    
    बटन प्रेस से निपटने के लिए `else` स्टेटमेंट का हिस्सा बनने के लिए कोड को मूव करें । यह सही जगह पर होने के लिए आपको इसे **इंडेंट (indent)** करना होगा।

- यदि आप इस कोड को चलाते हैं, तो आप देखेंगे कि यदि आप सही बटन को बहुत जल्दी दबाते हैं, तो भी प्रोग्राम आपको बहुत लंबा समय लेने की घोषणा करेगा। ऐसा इसलिए है क्योंकि आपने गेम को चेक करना बंद नहीं किया है यदि बटन दबाए जाने पर समय समाप्त हो जाता है। जब बटन दबाया जाता है तो कोड को यह बताने के लिए कि टाइमर को रोकना है अपने `button_pressed` फंक्शन बदलें।
    
    ```python
        def button_pressed(channel, event):
            print("You pressed " + str(channel) )
    
            explorerhat.light.off()
    
            global waiting_for_press
            waiting_for_press = False
    
    ```
    
    इस कोड में, `global` हमें फंक्शन के अंदर से वैरिएबल `waiting_for_press` का मूल्य बदलने की अनुमति देता है ।