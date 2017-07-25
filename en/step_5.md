## Turning lights on 

- You can use Python to tell the Explorer HAT which lights to turn on and off. Add the following new lines of code into your Python file, then run the program to see what it does:

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

    Can you work out how to do make your program do these things? 
    
    * Turn the other coloured lights on individually (blue, yellow, green)
    * Turn all of the lights off at once
    * Change the length of time for which the lights are turned on and off 

