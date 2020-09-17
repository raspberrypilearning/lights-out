## अनियमित(random) लाइब्रेरी का उपयोग करना

यह एक बहुत आसान खेल होगा अगर रोशनी हमेशा एक ही क्रम में, एक ही समय के लिए आए! खिलाड़ी के लिए जितना संभव हो उतना मुश्किल बनाने के लिए, आपको कुछ अनियमितता जोड़ने की आवश्यकता है। आप अनियमित करेंगे कि कौन सी लाइट चालू है, और अगली लाइट को चालू करने से पहले प्रोग्राम कितने समय तक इंतजार करेगा।

- अनियमित संख्या उत्पन्न करने के लिए, आपको Python के ` random `लाइब्रेरी का उपयोग करने की आवश्यकता है । अपने प्रोग्राम में उस लाइन को खोजें जो कहती है कि `from time import sleep `, और इसके नीचे टाइप करें `import random ` । इसके नीचे के सभी कोड को मिटा दें (जहां आपने रोशनी को चालू और बंद करने के साथ प्रयोग किया था)।

- सबसे पहले, आप Python को चालू करने के लिए एक अनियमित लाइट चुनने के लिए कहेंगे। इस कोड को अपने प्रोग्राम में जोड़ें:
    
    ```python
    light = random.randint(1,4)
    ```
    
    यह कोड 1 और 4 के बीच एक अनियमित पूर्णांक (पूरी संख्या) चुनता है और इसे वेरियबल `light` को असाइन करता है ।

- अब कुछ कोड जोड़कर एक लाइट चालू करें जो उस संख्या के आधार पर होती है जिसे अनियमितता से चुना गया था। क्या आप बाकी कोड खत्म कर सकते हैं? ध्यान दें कि 3 लाल बत्ती है और 4 हरी बत्ती है:
    
    ```python
    if light == 1:
        explorerhat.light.blue.on()
    elif light == 2:
        explorerhat.light.yellow.on()
    ```
    
    अपना प्रोग्राम कई बार Run करें। जांचें कि हर बार, जब कार्यक्रम चलता है, एक अलग रोशनी अनियमितता से चुनी जाती है। लाइट तुरंत चालू होना चाहिए।

- खेल को और अधिक मजेदार बनाने के लिए, रोशनी को चालू करने के बीच एक अननुमेय अंतर होना चाहिए, इसलिए कार्यक्रम को अगली रोशनी चालू करने से पहले कुछ समय के लिए प्रतीक्षा करने के लिए कुछ कोड जोड़ें:
    
    उस कोड के नीचे जहां आपने चुना था कि किस लाइट को चालू करना है, कोड की दो नई लाइनें जोड़ें:
    
    ```python
    light = random.randint(1,4)     
    
    wait_for_next = random.uniform(0.5, 3.5)
    sleep(wait_for_next)
    ```
    
    इस समय आप `random.uniform` फ़ंक्शन का उपयोग कर रहे हैं जो आपको भिन्नात्मक भागों (decimals) के साथ संख्या चुनने की अनुमति देता है। उपरोक्त कोड में, Python एक संख्या चुनता है जो आधे (0.5) और तीन और एक साढ़े (3.5) के बीच कुछ भी हो सकती है और फिर वो उतने सेकंड के लिए इंतजार करता है। आप इन मूल्यों को बदल सकते हैं यदि आप अपने खिलाड़ी के साथ अधिक (या कम) निर्दयी होना चाहते हैं!