## Een timer toevoegen

Nadat je een lamp hebt ingeschakeld, moet je een timer starten en controleren hoe lang het duurt voordat de speler op de knop drukt.

- Allereerst moet je Python vertellen om de tijdfunctie te importeren. Voeg na je andere `import` instructies de regel `from time import time` toe om aan Python te laten weten dat je de `time` functie wilt gebruiken.

- Ga naar de plek in je programma, net voor de regel waar gecontroleerd wordt of de knop wordt ingedrukt. Maak een variabele met de naam `start` om de huidige tijd op te nemen: deze wordt door je Raspberry Pi geleverd en is vrij nauwkeurig.
    
    ```python
    # ...andere code hier boven
    
    # Leg de huidige tijd vast
    start = time()
    
    # ... andere code hieronder
    
    ```

- Je kunt kiezen hoeveel seconden de speler op de knop moet drukken nadat een lampje is aangezet. Voeg een **constant** toe aan je programma net na de `game_in_progress` variabele met de waarde die je hebt gekozen. We kozen ervoor om onze speler 1,5 seconde toe te staan:
    
    ```python
    game_in_progress = True
    TIME_ALLOWED = 1.5
    
    ```
    
    Hoe kleiner het getal, hoe sneller de speler moet zijn!

- Voeg nu een lus toe om te controleren of de speler te lang heeft gewacht. Je kunt je voorstellen dat deze lus constant controleert of iemand op een lange autorit blijft vragen: "zijn we er al bijna?", "Zijn we er nu?", "Hoe zit het nu?"!
    
    ```python
    ...
    
    # Leg de huidige tijd vast
    start = time()
    
    waiting_for_press = True
    while waiting_for_press and game_in_progress:
    
        # Wat is de tijd nu?
        now = time()
        time_taken = now - start
    
        # Controleer of we te lang hebben gewacht
        if time_taken > TIME_ALLOWED:
            print("Je hebt te lang gewacht!")
            explorerhat.light.off()
            game_in_progress = False    # Spel verloren
    
        else:
            explorerhat.touch.pressed(button_pressed)
    
    
    ```
    
    Verplaats de code voor omgaan met button_pressed zodanig dat het deel uit te maakt van de `else` instructie. Je moet **inspringen** om ervoor te zorgen dat deze op de juiste plaats staat.

- Als je deze code uitvoert, zie je dat zelfs als je uiterst snel op de juiste knop drukt, het programma nog steeds zegt dat je te laat hebt gedrukt. Dit komt omdat je het spel niet hebt verteld om te stoppen met controleren of de tijd op is wanneer een knop wordt ingedrukt. Wijzig je `button_pressed` functie om de code te vertellen om de timer te stoppen wanneer een knop wordt ingedrukt.
    
    ```python
        def button_pressed(channel, event):
            print("Je drukte op " + str(channel) )
    
            explorerhat.light.off()
    
            global waiting_for_press
            waiting_for_press = False
    
    ```
    
    In deze code staat `global` ons toe om de waarde van de variabele `waiting_for_press` vanuit de functie te wijzigen.