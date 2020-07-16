## Pressing the button

- You need to know when the player presses a button on the Explorer HAT, and which button it was that they pressed. At the **bottom** of your code, add this line:
    
    ```python
    explorerhat.touch.pressed(button_pressed)
    ```

- When a button is pressed, the `button_pressed` function will be called, so you need to write this function. Put the following code at the **start** of your file, just after the `import` statements:
    
    ```python
    def button_pressed(channel, event):
        print("You pressed button " + str(channel) )
        explorerhat.light.off()
    ```
    
    The variable `channel` contains the number of the button that was pressed (1-4). Test your program and you should see that when you press a button, the number of the button you pressed will be displayed in the Python shell and all lights will be switched off.
    
    ![A message telling you which button was pressed](images/pressed-button.png)