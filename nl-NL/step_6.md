## De random (willekeurig) bibliotheek gebruiken

Dit zou een vrij eenvoudig spel zijn als de lichten altijd in dezelfde volgorde aan gingen, met dezelfde tijdsduur! Om het zo lastig mogelijk te maken voor de speler, moet je wat willekeur toevoegen. Je zult willekeurig bepalen welk licht is ingeschakeld en hoe lang het programma zal wachten voordat het volgende licht aan gaat.

- Om willekeurige getallen te genereren, moet je de `random` bibliotheek van Python gebruiken. Zoek de regel in je programma die `from time import sleep`, en typ daaronder `import random`. Verwijder alle onderliggende codes (waarin je hebt geprobeerd de lichten in en uit te schakelen).

- Eerst ga je Python vragen om een ​​willekeurig lampje te kiezen om in te schakelen. Voeg deze code toe aan je programma:
    
    ```python
    light = random.randint(1,4)
    ```
    
    Deze code kiest een willekeurig integer (geheel getal) tussen 1 en 4 en wijst dit toe aan de variabele `light`.

- Voeg nu een code toe om één licht in te schakelen afhankelijk van het nummer dat willekeurig is gekozen. Kun je de rest van de code afmaken? Merk op dat 3 het rode licht is en 4 het groene licht:
    
    ```python
    if light == 1:
        explorerhat.light.blue.on()
    elif light == 2:
        explorerhat.light.yellow.on()
    ```
    
    Run je programma meerdere keren. Controleer of elke keer dat het programma wordt uitgevoerd, er willekeurig een ander licht wordt gekozen. Het lampje moet onmiddellijk gaan branden.

- Om het spel leuker te maken, moet er een onvoorspelbare tijd zijn tussen de lichten die aan gaan, dus laten we wat code toevoegen om het programma een willekeurige tijd te laten wachten voordat het volgende licht wordt ingeschakeld:
    
    Onder de code waar je hebt gekozen welk licht je wilt inschakelen, voeg je twee nieuwe regels toe:
    
    ```python
    light = random.randint(1,4)     
    
    wait_for_next = random.uniform(0.5, 3.5)
    sleep(wait_for_next)
    ```
    
    Deze keer gebruik je de functie `random.uniform`, waarmee je getallen met decimalen kunt kiezen. In de bovenstaande code kiest Python een getal dat tussen de 0,5 en de 3,5 kan liggen en wacht dan dat aantal seconden. Je kunt deze waarden veranderen als je meer (of minder) gemeen wilt zijn voor je speler!