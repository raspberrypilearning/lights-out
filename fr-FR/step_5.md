## Allumer les lumières

- Tu peux utiliser Python pour indiquer à l'Explorer HAT les lumières à allumer et à éteindre. Ajoute les nouvelles lignes de code suivantes dans ton fichier Python, puis exécute le programme pour voir ce qu'il fait :
    
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
    
    Sais-tu trouver comment faire en sorte que ton programme fasse ces choses ?
    
    - Allumer les autres lumières colorées individuellement (bleu, jaune, vert)
    - Éteindre toutes les lumières en même temps
    - Modifier la durée de la mise en marche et de la désactivation des lumières