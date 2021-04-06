## Appuyer sur le bouton

- Tu dois savoir quand le joueur appuie sur un bouton de l'Explorer HAT, et sur quel bouton il a appuyé. Au **bas** de ton code, ajoute cette ligne :
    
    ```python
    explorerhat.touch.pressed(button_pressed)
    ```

- Lorsqu'un bouton est appuyé, la fonction `button_pressed` sera appelée, donc tu dois écrire cette fonction. Place le code suivant au **début** de ton fichier, juste après les instructions `import` :
    
    ```python
    def button_pressed(channel, event):
        print("Tu as appuyé sur le bouton " + str(channel) )
        explorerhat.light.off()
    ```
    
    La variable `channel` contient le numéro du bouton qui a été enfoncé (1-4). Teste ton programme et tu devrais voir que lorsque tu appuies sur un bouton, le numéro du bouton sur lequel tu as appuyé s'affiche dans le shell Python et toutes les lumières s'éteignent.
    
    ![Un message t'indiquant quel bouton a été appuyé](images/pressed-button.png)