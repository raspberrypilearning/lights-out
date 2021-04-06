## Mais était-ce le bon bouton ?

La dernière partie de notre jeu est de vérifier si le bouton que le joueur a appuyé était en fait le bon bouton. Pour faire çà, tu dois modifier à nouveau ta fonction `button_pressed`. Au début de la fonction, ajouter du code pour vérifier si la variable `light` (le numéro de la lumière choisie) est égale à la variable `channel` (le numéro du bouton appuyé) :

```python
def button_pressed(channel, event):
    if light == channel:
        print("Bien joué")
    else:
        print("Mauvais bouton")
        global game_in_progress
        game_in_progress = False
```

De nouveau, tu devras dire à Python que tu souhaites modifier la valeur de la variable `game_in_progress` depuis l'intérieur de la fonction en utilisant le mot `global`.

![Le jeu devrait maintenant détecter si le bon bouton a été appuyé](images/press-right-button.png)

C'est terminé ! Maintenant, teste ton jeu avec tes amis.