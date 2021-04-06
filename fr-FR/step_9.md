## Ajouter un minuteur

Une fois que tu allumes une lumière, tu dois démarrer un minuteur et vérifier combien de temps le joueur prend pour appuyer sur le bouton.

- Tout d'abord, tu devras dire à Python d'importer la fonction time (temps). À côté de tes autres instructions `import` , ajouter la ligne `from time import time` pour dire à Python que tu veux utiliser la fonction `time`.

- Va à l'endroit de ton programme juste avant la ligne de code vérifiant le bouton sur lequel tu appuies. Crée une variable appelée `start` pour enregistrer l'heure actuelle : elle sera fournie par ton Raspberry Pi et est assez précise.
    
    ```python
    # ...autre code ci-dessus
    
    # Enregistre l'heure actuelle
    start = time()
    
    # ... autre code ci-dessous
    
    ```

- Tu peux choisir combien de secondes le joueur aura pour appuyer sur le bouton une fois la lumière allumée. Ajoute une **constante** à ton programme juste après la variable `game_in_progress` avec la valeur que tu as choisie. Nous avons choisi d'accorder à notre joueur 1,5 secondes :
    
    ```python
    game_in_progress = True
    TIME_ALLOWED = 1.5
    
    ```
    
    Plus le nombre est petit, plus le joueur devra être rapide !

- Ajoute maintenant une boucle pour continuer à vérifier si l'utilisateur a dépassé le temps qui lui était imparti. La vérification constante de cette boucle peut être comparée à celle d'une personne qui, lors d'un long voyage en voiture, demande sans cesse : « On est bientôt arrivé ? », « On est arrivé maintenant ? », « Et maintenant ? ».
    
    ```python
    ...
    
    # Enregistre l'heure actuelle
    start = time()
    
    waiting_for_press = True
    while waiting_for_press and game_in_progress:
    
        # Quelle heure est-il maintenant ?
        now = time()
        time_taken = now - start
    
        # Vérifie s'ils ont pris plus de temps qu'ils n'étaient autorisés.
        if time_taken > TIME_ALLOWED:
            print("Tu as pris trop de temps !")
            explorerhat.light.off()
            game_in_progress = False    # Perd la partie
    
        else:
            explorerhat.touch.pressed(button_pressed)
    
    
    ```
    
    Déplace le code pour gérer les pressions sur les boutons pour qu'il fasse partie de l'instruction `else`. Tu devras **indenter** pour qu'il soit au bon endroit.

- Si tu exécutes ce code, tu verras que même si tu appuies sur le bon bouton très rapidement, le programme continuera de dire que tu as pris trop de temps. C'est parce que tu n'as pas dit au jeu d'arrêter de vérifier si le temps est écoulé quand un bouton est appuyé. Modifie ta fonction `button_pressed` pour dire au code d'arrêter le minuteur lorsqu'un bouton est appuyé.
    
    ```python
        def button_pressed(channel, event):
            print("Tu as appuyé " + str(channel) )
    
            explorerhat.light.off()
    
            global waiting_for_press
            waiting_for_press = False
    
    ```
    
    Dans ce code, `global` nous permet de changer la valeur de la variable `waiting_for_press` depuis l'intérieur de la fonction.