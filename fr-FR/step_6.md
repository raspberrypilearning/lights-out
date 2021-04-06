## Utiliser le module random

Ce serait un jeu trop facile si les lumières s'allumaient toujours dans le même ordre et la même durée ! Pour compliquer les choses pour le joueur, tu dois ajouter un peu de hasard. Tu vas aléatoirement déterminer quelle lumière est allumée et combien de temps le programme attendra avant d'allumer la lumière suivante.

- Pour générer des nombres aléatoires, tu dois utiliser le module `random` de Python. Trouve la ligne dans ton programme qui dit `from time import sleep`, et en dessous de cette ligne, tape `import random`. Supprime tout le code situé en dessous (où tu as expérimenté l'allumage et l'extinction des lumières).

- Tout d'abord, tu vas demander à Python de choisir une lumière aléatoire à allumer. Ajoute ce code à ton programme :
    
    ```python
    light = random.randint(1,4)
    ```
    
    Ce code choisit un entier aléatoire (nombre entier) entre 1 et 4 et l'assigne à la variable `light`.

- Maintenant, ajoute du code pour allumer une lumière en fonction du nombre qui a été choisi aléatoirement. Peux-tu terminer le reste du code ? Note que 3 est la lumière rouge et 4 est la lumière verte :
    
    ```python
    if light == 1:
        explorerhat.light.blue.on()
    elif light == 2:
        explorerhat.light.yellow.on()
    ```
    
    Exécute ton programme plusieurs fois. Vérifie que, chaque fois que le programme s'exécute, une lumière différente est choisie aléatoirement. La lumière doit s'allumer immédiatement.

- Pour rendre le jeu plus amusant, il doit y avoir un écart imprévisible entre les lumières qui s'allument. Ajoutons donc du code pour que le programme attende un temps aléatoire avant d'allumer la lumière suivante :
    
    Sous le code où tu as choisi quelle lumière allumer, ajoute deux nouvelles lignes de code :
    
    ```python
    light = random.randint(1,4)     
    
    wait_for_next = random.uniform(0.5, 3.5)
    sleep(wait_for_next)
    ```
    
    Cette fois, tu utilises la fonction `random.uniform` qui te permet de choisir des nombres avec des parties fractionnaires (décimales). Dans le code ci-dessus, Python choisit un nombre qui peut être compris entre la moitié (0,5) et trois et demi (3,5), puis attend ce nombre de secondes. Tu peux modifier ces valeurs si tu souhaites être plus (ou moins) malicieux avec ton joueur !