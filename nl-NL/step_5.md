## Zet de lichten aan

- Je kunt Python gebruiken om de Explorer HAT te vertellen welke lampjes moeten worden in- en uitgeschakeld. Voeg de volgende nieuwe regels code toe aan je Python-bestand en voer het programma uit om te zien wat het doet:
    
    ```python
    import explorerhat
    from time import sleep
    
    explorerhat.light.red.on()
    sleep(2)
    explorerhat.light.red.off()
    sleep(1)
    explorerhat.light.on()
    sleep(5)
    ```
    
   Kun jij uitvinden hoe jouw programma deze dingen laat gebeuren?
    
    - Zet de andere gekleurde lichten (blauw, geel, groen) individueel aan
    - Schakel alle lichten in één keer uit
    - Verander de tijdsduur waarin de verlichting wordt in- en uitgeschakeld